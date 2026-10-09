"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#PinpointSMSVoiceV2``."""

import datetime
import uuid
import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_pinpoint_sms_voice_v2._auth._signers
import capo_pinpoint_sms_voice_v2._auth._sigv4
from capo_pinpoint_sms_voice_v2._auth._identity import Credentials
from capo_pinpoint_sms_voice_v2._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_pinpoint_sms_voice_v2._auth._zapros_handler import AuthMiddleware
from capo_pinpoint_sms_voice_v2._services._aws_config import aaws_config
from capo_pinpoint_sms_voice_v2._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.amazon_resource_name
    import capo_pinpoint_sms_voice_v2.types.associate_origination_identity_request
    import capo_pinpoint_sms_voice_v2.types.associate_origination_identity_result
    import capo_pinpoint_sms_voice_v2.types.associate_protect_configuration_request
    import capo_pinpoint_sms_voice_v2.types.associate_protect_configuration_result
    import capo_pinpoint_sms_voice_v2.types.attachment_body
    import capo_pinpoint_sms_voice_v2.types.attachment_url
    import capo_pinpoint_sms_voice_v2.types.carrier_lookup_input_phone_number_type
    import capo_pinpoint_sms_voice_v2.types.carrier_lookup_request
    import capo_pinpoint_sms_voice_v2.types.carrier_lookup_result
    import capo_pinpoint_sms_voice_v2.types.client_token
    import capo_pinpoint_sms_voice_v2.types.cloud_watch_logs_destination
    import capo_pinpoint_sms_voice_v2.types.configuration_set_filter_list
    import capo_pinpoint_sms_voice_v2.types.configuration_set_name
    import capo_pinpoint_sms_voice_v2.types.configuration_set_name_list
    import capo_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn
    import capo_pinpoint_sms_voice_v2.types.context_map
    import capo_pinpoint_sms_voice_v2.types.country_launch_status_filter_list
    import capo_pinpoint_sms_voice_v2.types.create_configuration_set_request
    import capo_pinpoint_sms_voice_v2.types.create_configuration_set_result
    import capo_pinpoint_sms_voice_v2.types.create_event_destination_request
    import capo_pinpoint_sms_voice_v2.types.create_event_destination_result
    import capo_pinpoint_sms_voice_v2.types.create_notify_configuration_request
    import capo_pinpoint_sms_voice_v2.types.create_notify_configuration_result
    import capo_pinpoint_sms_voice_v2.types.create_opt_out_list_request
    import capo_pinpoint_sms_voice_v2.types.create_opt_out_list_result
    import capo_pinpoint_sms_voice_v2.types.create_pool_request
    import capo_pinpoint_sms_voice_v2.types.create_pool_result
    import capo_pinpoint_sms_voice_v2.types.create_protect_configuration_request
    import capo_pinpoint_sms_voice_v2.types.create_protect_configuration_result
    import capo_pinpoint_sms_voice_v2.types.create_rcs_agent_request
    import capo_pinpoint_sms_voice_v2.types.create_rcs_agent_result
    import capo_pinpoint_sms_voice_v2.types.create_registration_association_request
    import capo_pinpoint_sms_voice_v2.types.create_registration_association_result
    import capo_pinpoint_sms_voice_v2.types.create_registration_attachment_request
    import capo_pinpoint_sms_voice_v2.types.create_registration_attachment_result
    import capo_pinpoint_sms_voice_v2.types.create_registration_request
    import capo_pinpoint_sms_voice_v2.types.create_registration_result
    import capo_pinpoint_sms_voice_v2.types.create_registration_version_request
    import capo_pinpoint_sms_voice_v2.types.create_registration_version_result
    import capo_pinpoint_sms_voice_v2.types.create_verified_destination_number_request
    import capo_pinpoint_sms_voice_v2.types.create_verified_destination_number_result
    import capo_pinpoint_sms_voice_v2.types.delete_account_default_protect_configuration_request
    import capo_pinpoint_sms_voice_v2.types.delete_account_default_protect_configuration_result
    import capo_pinpoint_sms_voice_v2.types.delete_configuration_set_request
    import capo_pinpoint_sms_voice_v2.types.delete_configuration_set_result
    import capo_pinpoint_sms_voice_v2.types.delete_default_message_type_request
    import capo_pinpoint_sms_voice_v2.types.delete_default_message_type_result
    import capo_pinpoint_sms_voice_v2.types.delete_default_sender_id_request
    import capo_pinpoint_sms_voice_v2.types.delete_default_sender_id_result
    import capo_pinpoint_sms_voice_v2.types.delete_event_destination_request
    import capo_pinpoint_sms_voice_v2.types.delete_event_destination_result
    import capo_pinpoint_sms_voice_v2.types.delete_keyword_request
    import capo_pinpoint_sms_voice_v2.types.delete_keyword_result
    import capo_pinpoint_sms_voice_v2.types.delete_media_message_spend_limit_override_request
    import capo_pinpoint_sms_voice_v2.types.delete_media_message_spend_limit_override_result
    import capo_pinpoint_sms_voice_v2.types.delete_notify_configuration_request
    import capo_pinpoint_sms_voice_v2.types.delete_notify_configuration_result
    import capo_pinpoint_sms_voice_v2.types.delete_notify_message_spend_limit_override_request
    import capo_pinpoint_sms_voice_v2.types.delete_notify_message_spend_limit_override_result
    import capo_pinpoint_sms_voice_v2.types.delete_opt_out_list_request
    import capo_pinpoint_sms_voice_v2.types.delete_opt_out_list_result
    import capo_pinpoint_sms_voice_v2.types.delete_opted_out_number_request
    import capo_pinpoint_sms_voice_v2.types.delete_opted_out_number_result
    import capo_pinpoint_sms_voice_v2.types.delete_pool_request
    import capo_pinpoint_sms_voice_v2.types.delete_pool_result
    import capo_pinpoint_sms_voice_v2.types.delete_protect_configuration_request
    import capo_pinpoint_sms_voice_v2.types.delete_protect_configuration_result
    import capo_pinpoint_sms_voice_v2.types.delete_protect_configuration_rule_set_number_override_request
    import capo_pinpoint_sms_voice_v2.types.delete_protect_configuration_rule_set_number_override_result
    import capo_pinpoint_sms_voice_v2.types.delete_rcs_agent_request
    import capo_pinpoint_sms_voice_v2.types.delete_rcs_agent_result
    import capo_pinpoint_sms_voice_v2.types.delete_rcs_message_spend_limit_override_request
    import capo_pinpoint_sms_voice_v2.types.delete_rcs_message_spend_limit_override_result
    import capo_pinpoint_sms_voice_v2.types.delete_registration_attachment_request
    import capo_pinpoint_sms_voice_v2.types.delete_registration_attachment_result
    import capo_pinpoint_sms_voice_v2.types.delete_registration_field_value_request
    import capo_pinpoint_sms_voice_v2.types.delete_registration_field_value_result
    import capo_pinpoint_sms_voice_v2.types.delete_registration_request
    import capo_pinpoint_sms_voice_v2.types.delete_registration_result
    import capo_pinpoint_sms_voice_v2.types.delete_resource_policy_request
    import capo_pinpoint_sms_voice_v2.types.delete_resource_policy_result
    import capo_pinpoint_sms_voice_v2.types.delete_text_message_spend_limit_override_request
    import capo_pinpoint_sms_voice_v2.types.delete_text_message_spend_limit_override_result
    import capo_pinpoint_sms_voice_v2.types.delete_verified_destination_number_request
    import capo_pinpoint_sms_voice_v2.types.delete_verified_destination_number_result
    import capo_pinpoint_sms_voice_v2.types.delete_voice_message_spend_limit_override_request
    import capo_pinpoint_sms_voice_v2.types.delete_voice_message_spend_limit_override_result
    import capo_pinpoint_sms_voice_v2.types.describe_account_attributes_request
    import capo_pinpoint_sms_voice_v2.types.describe_account_attributes_result
    import capo_pinpoint_sms_voice_v2.types.describe_account_limits_request
    import capo_pinpoint_sms_voice_v2.types.describe_account_limits_result
    import capo_pinpoint_sms_voice_v2.types.describe_configuration_sets_request
    import capo_pinpoint_sms_voice_v2.types.describe_configuration_sets_result
    import capo_pinpoint_sms_voice_v2.types.describe_keywords_request
    import capo_pinpoint_sms_voice_v2.types.describe_keywords_result
    import capo_pinpoint_sms_voice_v2.types.describe_notify_configurations_request
    import capo_pinpoint_sms_voice_v2.types.describe_notify_configurations_result
    import capo_pinpoint_sms_voice_v2.types.describe_notify_templates_request
    import capo_pinpoint_sms_voice_v2.types.describe_notify_templates_result
    import capo_pinpoint_sms_voice_v2.types.describe_opt_out_lists_request
    import capo_pinpoint_sms_voice_v2.types.describe_opt_out_lists_result
    import capo_pinpoint_sms_voice_v2.types.describe_opted_out_numbers_request
    import capo_pinpoint_sms_voice_v2.types.describe_opted_out_numbers_result
    import capo_pinpoint_sms_voice_v2.types.describe_phone_numbers_request
    import capo_pinpoint_sms_voice_v2.types.describe_phone_numbers_result
    import capo_pinpoint_sms_voice_v2.types.describe_pools_request
    import capo_pinpoint_sms_voice_v2.types.describe_pools_result
    import capo_pinpoint_sms_voice_v2.types.describe_protect_configurations_request
    import capo_pinpoint_sms_voice_v2.types.describe_protect_configurations_result
    import capo_pinpoint_sms_voice_v2.types.describe_rcs_agent_country_launch_status_request
    import capo_pinpoint_sms_voice_v2.types.describe_rcs_agent_country_launch_status_result
    import capo_pinpoint_sms_voice_v2.types.describe_rcs_agents_request
    import capo_pinpoint_sms_voice_v2.types.describe_rcs_agents_result
    import capo_pinpoint_sms_voice_v2.types.describe_registration_attachments_request
    import capo_pinpoint_sms_voice_v2.types.describe_registration_attachments_result
    import capo_pinpoint_sms_voice_v2.types.describe_registration_field_definitions_request
    import capo_pinpoint_sms_voice_v2.types.describe_registration_field_definitions_result
    import capo_pinpoint_sms_voice_v2.types.describe_registration_field_values_request
    import capo_pinpoint_sms_voice_v2.types.describe_registration_field_values_result
    import capo_pinpoint_sms_voice_v2.types.describe_registration_section_definitions_request
    import capo_pinpoint_sms_voice_v2.types.describe_registration_section_definitions_result
    import capo_pinpoint_sms_voice_v2.types.describe_registration_type_definitions_request
    import capo_pinpoint_sms_voice_v2.types.describe_registration_type_definitions_result
    import capo_pinpoint_sms_voice_v2.types.describe_registration_versions_request
    import capo_pinpoint_sms_voice_v2.types.describe_registration_versions_result
    import capo_pinpoint_sms_voice_v2.types.describe_registrations_request
    import capo_pinpoint_sms_voice_v2.types.describe_registrations_result
    import capo_pinpoint_sms_voice_v2.types.describe_sender_ids_request
    import capo_pinpoint_sms_voice_v2.types.describe_sender_ids_result
    import capo_pinpoint_sms_voice_v2.types.describe_spend_limits_request
    import capo_pinpoint_sms_voice_v2.types.describe_spend_limits_result
    import capo_pinpoint_sms_voice_v2.types.describe_verified_destination_numbers_request
    import capo_pinpoint_sms_voice_v2.types.describe_verified_destination_numbers_result
    import capo_pinpoint_sms_voice_v2.types.destination_country_parameters
    import capo_pinpoint_sms_voice_v2.types.destination_phone_number_list
    import capo_pinpoint_sms_voice_v2.types.disassociate_origination_identity_request
    import capo_pinpoint_sms_voice_v2.types.disassociate_origination_identity_result
    import capo_pinpoint_sms_voice_v2.types.disassociate_protect_configuration_request
    import capo_pinpoint_sms_voice_v2.types.disassociate_protect_configuration_result
    import capo_pinpoint_sms_voice_v2.types.discard_registration_version_request
    import capo_pinpoint_sms_voice_v2.types.discard_registration_version_result
    import capo_pinpoint_sms_voice_v2.types.event_destination_name
    import capo_pinpoint_sms_voice_v2.types.event_type_list
    import capo_pinpoint_sms_voice_v2.types.field_path
    import capo_pinpoint_sms_voice_v2.types.field_path_list
    import capo_pinpoint_sms_voice_v2.types.get_protect_configuration_country_rule_set_request
    import capo_pinpoint_sms_voice_v2.types.get_protect_configuration_country_rule_set_result
    import capo_pinpoint_sms_voice_v2.types.get_resource_policy_request
    import capo_pinpoint_sms_voice_v2.types.get_resource_policy_result
    import capo_pinpoint_sms_voice_v2.types.iam_role_arn
    import capo_pinpoint_sms_voice_v2.types.iam_role_arn_or_unset
    import capo_pinpoint_sms_voice_v2.types.iso_country_code
    import capo_pinpoint_sms_voice_v2.types.iso_country_code_list
    import capo_pinpoint_sms_voice_v2.types.keyword
    import capo_pinpoint_sms_voice_v2.types.keyword_action
    import capo_pinpoint_sms_voice_v2.types.keyword_filter_list
    import capo_pinpoint_sms_voice_v2.types.keyword_list
    import capo_pinpoint_sms_voice_v2.types.keyword_message
    import capo_pinpoint_sms_voice_v2.types.kinesis_firehose_destination
    import capo_pinpoint_sms_voice_v2.types.language_code
    import capo_pinpoint_sms_voice_v2.types.list_available_phone_numbers_max_results
    import capo_pinpoint_sms_voice_v2.types.list_available_phone_numbers_request
    import capo_pinpoint_sms_voice_v2.types.list_available_phone_numbers_result
    import capo_pinpoint_sms_voice_v2.types.list_notify_countries_request
    import capo_pinpoint_sms_voice_v2.types.list_notify_countries_result
    import capo_pinpoint_sms_voice_v2.types.list_pool_origination_identities_request
    import capo_pinpoint_sms_voice_v2.types.list_pool_origination_identities_result
    import capo_pinpoint_sms_voice_v2.types.list_protect_configuration_rule_set_number_override_filter
    import capo_pinpoint_sms_voice_v2.types.list_protect_configuration_rule_set_number_overrides_request
    import capo_pinpoint_sms_voice_v2.types.list_protect_configuration_rule_set_number_overrides_result
    import capo_pinpoint_sms_voice_v2.types.list_registration_associations_request
    import capo_pinpoint_sms_voice_v2.types.list_registration_associations_result
    import capo_pinpoint_sms_voice_v2.types.list_tags_for_resource_request
    import capo_pinpoint_sms_voice_v2.types.list_tags_for_resource_result
    import capo_pinpoint_sms_voice_v2.types.max_price
    import capo_pinpoint_sms_voice_v2.types.max_results
    import capo_pinpoint_sms_voice_v2.types.media_message_origination_identity
    import capo_pinpoint_sms_voice_v2.types.media_url_list
    import capo_pinpoint_sms_voice_v2.types.message_feedback_status
    import capo_pinpoint_sms_voice_v2.types.message_id
    import capo_pinpoint_sms_voice_v2.types.message_type
    import capo_pinpoint_sms_voice_v2.types.message_type_list
    import capo_pinpoint_sms_voice_v2.types.monthly_limit
    import capo_pinpoint_sms_voice_v2.types.next_token
    import capo_pinpoint_sms_voice_v2.types.non_empty_tag_list
    import capo_pinpoint_sms_voice_v2.types.notify_configuration_display_name
    import capo_pinpoint_sms_voice_v2.types.notify_configuration_filter_list
    import capo_pinpoint_sms_voice_v2.types.notify_configuration_id_list
    import capo_pinpoint_sms_voice_v2.types.notify_configuration_id_or_arn
    import capo_pinpoint_sms_voice_v2.types.notify_configuration_tier
    import capo_pinpoint_sms_voice_v2.types.notify_configuration_use_case
    import capo_pinpoint_sms_voice_v2.types.notify_enabled_channels_list
    import capo_pinpoint_sms_voice_v2.types.notify_pool_id_or_unset
    import capo_pinpoint_sms_voice_v2.types.notify_template_filter_list
    import capo_pinpoint_sms_voice_v2.types.notify_template_id
    import capo_pinpoint_sms_voice_v2.types.notify_template_id_list
    import capo_pinpoint_sms_voice_v2.types.notify_use_case_list
    import capo_pinpoint_sms_voice_v2.types.number_capability
    import capo_pinpoint_sms_voice_v2.types.number_capability_list
    import capo_pinpoint_sms_voice_v2.types.number_preference_list
    import capo_pinpoint_sms_voice_v2.types.opt_out_list_name
    import capo_pinpoint_sms_voice_v2.types.opt_out_list_name_list
    import capo_pinpoint_sms_voice_v2.types.opt_out_list_name_or_arn
    import capo_pinpoint_sms_voice_v2.types.opted_out_filter_list
    import capo_pinpoint_sms_voice_v2.types.opted_out_number_list
    import capo_pinpoint_sms_voice_v2.types.owner
    import capo_pinpoint_sms_voice_v2.types.phone_number
    import capo_pinpoint_sms_voice_v2.types.phone_number_filter_list
    import capo_pinpoint_sms_voice_v2.types.phone_number_id_list
    import capo_pinpoint_sms_voice_v2.types.phone_number_id_or_arn
    import capo_pinpoint_sms_voice_v2.types.phone_or_pool_id_or_arn
    import capo_pinpoint_sms_voice_v2.types.phone_or_sender_id_or_arn
    import capo_pinpoint_sms_voice_v2.types.pool_filter_list
    import capo_pinpoint_sms_voice_v2.types.pool_id_list
    import capo_pinpoint_sms_voice_v2.types.pool_id_or_arn
    import capo_pinpoint_sms_voice_v2.types.pool_origination_identities_filter_list
    import capo_pinpoint_sms_voice_v2.types.protect_configuration_country_rule_set
    import capo_pinpoint_sms_voice_v2.types.protect_configuration_filter_list
    import capo_pinpoint_sms_voice_v2.types.protect_configuration_id_list
    import capo_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn
    import capo_pinpoint_sms_voice_v2.types.protect_configuration_rule_override_action
    import capo_pinpoint_sms_voice_v2.types.put_keyword_request
    import capo_pinpoint_sms_voice_v2.types.put_keyword_result
    import capo_pinpoint_sms_voice_v2.types.put_message_feedback_request
    import capo_pinpoint_sms_voice_v2.types.put_message_feedback_result
    import capo_pinpoint_sms_voice_v2.types.put_opted_out_number_request
    import capo_pinpoint_sms_voice_v2.types.put_opted_out_number_result
    import capo_pinpoint_sms_voice_v2.types.put_protect_configuration_rule_set_number_override_request
    import capo_pinpoint_sms_voice_v2.types.put_protect_configuration_rule_set_number_override_result
    import capo_pinpoint_sms_voice_v2.types.put_registration_field_value_request
    import capo_pinpoint_sms_voice_v2.types.put_registration_field_value_result
    import capo_pinpoint_sms_voice_v2.types.put_resource_policy_request
    import capo_pinpoint_sms_voice_v2.types.put_resource_policy_result
    import capo_pinpoint_sms_voice_v2.types.rcs_agent_filter_list
    import capo_pinpoint_sms_voice_v2.types.rcs_agent_id_list
    import capo_pinpoint_sms_voice_v2.types.rcs_agent_id_or_arn
    import capo_pinpoint_sms_voice_v2.types.rcs_event_type_list
    import capo_pinpoint_sms_voice_v2.types.rcs_fallback_configuration
    import capo_pinpoint_sms_voice_v2.types.rcs_message_content
    import capo_pinpoint_sms_voice_v2.types.rcs_message_origination_identity
    import capo_pinpoint_sms_voice_v2.types.rcs_message_traffic_type
    import capo_pinpoint_sms_voice_v2.types.rcs_time_to_live
    import capo_pinpoint_sms_voice_v2.types.registration_association_filter_list
    import capo_pinpoint_sms_voice_v2.types.registration_attachment_filter_list
    import capo_pinpoint_sms_voice_v2.types.registration_attachment_id_list
    import capo_pinpoint_sms_voice_v2.types.registration_attachment_id_or_arn
    import capo_pinpoint_sms_voice_v2.types.registration_filter_list
    import capo_pinpoint_sms_voice_v2.types.registration_id_list
    import capo_pinpoint_sms_voice_v2.types.registration_id_or_arn
    import capo_pinpoint_sms_voice_v2.types.registration_type
    import capo_pinpoint_sms_voice_v2.types.registration_type_filter_list
    import capo_pinpoint_sms_voice_v2.types.registration_type_list
    import capo_pinpoint_sms_voice_v2.types.registration_version_filter_list
    import capo_pinpoint_sms_voice_v2.types.registration_version_number
    import capo_pinpoint_sms_voice_v2.types.registration_version_number_list
    import capo_pinpoint_sms_voice_v2.types.release_phone_number_request
    import capo_pinpoint_sms_voice_v2.types.release_phone_number_result
    import capo_pinpoint_sms_voice_v2.types.release_sender_id_request
    import capo_pinpoint_sms_voice_v2.types.release_sender_id_result
    import capo_pinpoint_sms_voice_v2.types.request_phone_number_request
    import capo_pinpoint_sms_voice_v2.types.request_phone_number_result
    import capo_pinpoint_sms_voice_v2.types.request_sender_id_request
    import capo_pinpoint_sms_voice_v2.types.request_sender_id_result
    import capo_pinpoint_sms_voice_v2.types.requestable_number_type
    import capo_pinpoint_sms_voice_v2.types.resource_id_or_arn
    import capo_pinpoint_sms_voice_v2.types.resource_policy
    import capo_pinpoint_sms_voice_v2.types.searchable_number_type
    import capo_pinpoint_sms_voice_v2.types.section_path
    import capo_pinpoint_sms_voice_v2.types.section_path_list
    import capo_pinpoint_sms_voice_v2.types.select_choice_list
    import capo_pinpoint_sms_voice_v2.types.send_destination_number_verification_code_request
    import capo_pinpoint_sms_voice_v2.types.send_destination_number_verification_code_result
    import capo_pinpoint_sms_voice_v2.types.send_media_message_request
    import capo_pinpoint_sms_voice_v2.types.send_media_message_result
    import capo_pinpoint_sms_voice_v2.types.send_notify_text_message_request
    import capo_pinpoint_sms_voice_v2.types.send_notify_text_message_result
    import capo_pinpoint_sms_voice_v2.types.send_notify_voice_message_request
    import capo_pinpoint_sms_voice_v2.types.send_notify_voice_message_result
    import capo_pinpoint_sms_voice_v2.types.send_rcs_message_request
    import capo_pinpoint_sms_voice_v2.types.send_rcs_message_result
    import capo_pinpoint_sms_voice_v2.types.send_text_message_request
    import capo_pinpoint_sms_voice_v2.types.send_text_message_result
    import capo_pinpoint_sms_voice_v2.types.send_voice_message_request
    import capo_pinpoint_sms_voice_v2.types.send_voice_message_result
    import capo_pinpoint_sms_voice_v2.types.sender_id
    import capo_pinpoint_sms_voice_v2.types.sender_id_filter_list
    import capo_pinpoint_sms_voice_v2.types.sender_id_list
    import capo_pinpoint_sms_voice_v2.types.sender_id_or_arn
    import capo_pinpoint_sms_voice_v2.types.set_account_default_protect_configuration_request
    import capo_pinpoint_sms_voice_v2.types.set_account_default_protect_configuration_result
    import capo_pinpoint_sms_voice_v2.types.set_default_message_feedback_enabled_request
    import capo_pinpoint_sms_voice_v2.types.set_default_message_feedback_enabled_result
    import capo_pinpoint_sms_voice_v2.types.set_default_message_type_request
    import capo_pinpoint_sms_voice_v2.types.set_default_message_type_result
    import capo_pinpoint_sms_voice_v2.types.set_default_sender_id_request
    import capo_pinpoint_sms_voice_v2.types.set_default_sender_id_result
    import capo_pinpoint_sms_voice_v2.types.set_media_message_spend_limit_override_request
    import capo_pinpoint_sms_voice_v2.types.set_media_message_spend_limit_override_result
    import capo_pinpoint_sms_voice_v2.types.set_notify_message_spend_limit_override_request
    import capo_pinpoint_sms_voice_v2.types.set_notify_message_spend_limit_override_result
    import capo_pinpoint_sms_voice_v2.types.set_rcs_message_spend_limit_override_request
    import capo_pinpoint_sms_voice_v2.types.set_rcs_message_spend_limit_override_result
    import capo_pinpoint_sms_voice_v2.types.set_text_message_spend_limit_override_request
    import capo_pinpoint_sms_voice_v2.types.set_text_message_spend_limit_override_result
    import capo_pinpoint_sms_voice_v2.types.set_voice_message_spend_limit_override_request
    import capo_pinpoint_sms_voice_v2.types.set_voice_message_spend_limit_override_result
    import capo_pinpoint_sms_voice_v2.types.sns_destination
    import capo_pinpoint_sms_voice_v2.types.submit_registration_version_request
    import capo_pinpoint_sms_voice_v2.types.submit_registration_version_result
    import capo_pinpoint_sms_voice_v2.types.tag_key_list
    import capo_pinpoint_sms_voice_v2.types.tag_list
    import capo_pinpoint_sms_voice_v2.types.tag_resource_request
    import capo_pinpoint_sms_voice_v2.types.tag_resource_result
    import capo_pinpoint_sms_voice_v2.types.template_variable_substitution_map
    import capo_pinpoint_sms_voice_v2.types.text_message_body
    import capo_pinpoint_sms_voice_v2.types.text_message_origination_identity
    import capo_pinpoint_sms_voice_v2.types.text_value
    import capo_pinpoint_sms_voice_v2.types.time_to_live
    import capo_pinpoint_sms_voice_v2.types.two_way_channel_arn
    import capo_pinpoint_sms_voice_v2.types.two_way_media_s3_bucket_name_or_unset
    import capo_pinpoint_sms_voice_v2.types.two_way_media_s3_key_prefix
    import capo_pinpoint_sms_voice_v2.types.untag_resource_request
    import capo_pinpoint_sms_voice_v2.types.untag_resource_result
    import capo_pinpoint_sms_voice_v2.types.update_event_destination_request
    import capo_pinpoint_sms_voice_v2.types.update_event_destination_result
    import capo_pinpoint_sms_voice_v2.types.update_notify_configuration_request
    import capo_pinpoint_sms_voice_v2.types.update_notify_configuration_result
    import capo_pinpoint_sms_voice_v2.types.update_phone_number_request
    import capo_pinpoint_sms_voice_v2.types.update_phone_number_result
    import capo_pinpoint_sms_voice_v2.types.update_pool_request
    import capo_pinpoint_sms_voice_v2.types.update_pool_result
    import capo_pinpoint_sms_voice_v2.types.update_protect_configuration_country_rule_set_request
    import capo_pinpoint_sms_voice_v2.types.update_protect_configuration_country_rule_set_result
    import capo_pinpoint_sms_voice_v2.types.update_protect_configuration_request
    import capo_pinpoint_sms_voice_v2.types.update_protect_configuration_result
    import capo_pinpoint_sms_voice_v2.types.update_rcs_agent_request
    import capo_pinpoint_sms_voice_v2.types.update_rcs_agent_result
    import capo_pinpoint_sms_voice_v2.types.update_sender_id_request
    import capo_pinpoint_sms_voice_v2.types.update_sender_id_result
    import capo_pinpoint_sms_voice_v2.types.verification_channel
    import capo_pinpoint_sms_voice_v2.types.verification_code
    import capo_pinpoint_sms_voice_v2.types.verification_message_origination_identity
    import capo_pinpoint_sms_voice_v2.types.verified_destination_number_filter_list
    import capo_pinpoint_sms_voice_v2.types.verified_destination_number_id_list
    import capo_pinpoint_sms_voice_v2.types.verified_destination_number_id_or_arn
    import capo_pinpoint_sms_voice_v2.types.verify_destination_number_request
    import capo_pinpoint_sms_voice_v2.types.verify_destination_number_result
    import capo_pinpoint_sms_voice_v2.types.voice_id
    import capo_pinpoint_sms_voice_v2.types.voice_message_body
    import capo_pinpoint_sms_voice_v2.types.voice_message_body_text_type
    import capo_pinpoint_sms_voice_v2.types.voice_message_origination_identity


class AsyncPinpointSMSVoiceV2ClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncPinpointSMSVoiceV2Client:
    """A client for the ``PinpointSMSVoiceV2`` service.

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
        self._config = AsyncPinpointSMSVoiceV2ClientConfig(
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
        self, config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncPinpointSMSVoiceV2ClientConfig = config_overrides or {}
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

    async def associate_origination_identity(
        self,
        pool_id: "capo_pinpoint_sms_voice_v2.types.pool_id_or_arn.PoolIdOrArn",
        origination_identity: "capo_pinpoint_sms_voice_v2.types.phone_or_sender_id_or_arn.PhoneOrSenderIdOrArn",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        iso_country_code: Optional[
            "capo_pinpoint_sms_voice_v2.types.iso_country_code.IsoCountryCode"
        ] = None,
        client_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.associate_origination_identity_result.AssociateOriginationIdentityResult":
        """<p>Associates the specified origination identity with a pool.</p> <p>If the origination identity is a phone number and is already associated with another pool, an error is returned. A sender ID can be associated with multiple pools.</p> <p>If the origination identity configuration doesn't match the pool's configuration, an error is returned.</p>

        Args:
            pool_id: <p>The pool to update with the new Identity. This value can be either the PoolId or PoolArn, and you can find these values using <a href="https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribePools.html">DescribePools</a>.</p> <important> <p>If you are using a shared End User Messaging SMS; resource then you must use the full Amazon Resource Name(ARN).</p> </important>
            origination_identity: <p>The origination identity to use, such as PhoneNumberId, PhoneNumberArn, SenderId, or SenderIdArn. You can use <a>DescribePhoneNumbers</a> to find the values for PhoneNumberId and PhoneNumberArn, while <a>DescribeSenderIds</a> can be used to get the values for SenderId and SenderIdArn.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>
            iso_country_code: <p>The new two-character code, in ISO 3166-1 alpha-2 format, for the country or region of the origination identity. This field is optional and is not required for origination identity types that are not country-specific, such as RCS agents.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.associate_origination_identity_request.AssociateOriginationIdentityRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.associate_origination_identity_result.AssociateOriginationIdentityResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.associate_origination_identity

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.associate_origination_identity.async_associate_origination_identity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.associate_origination_identity_request.AssociateOriginationIdentityRequest = {
            "pool_id": pool_id,
            "origination_identity": origination_identity,
        }
        if iso_country_code is not None:
            input_["iso_country_code"] = iso_country_code
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

    async def associate_protect_configuration(
        self,
        protect_configuration_id: "capo_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn.ProtectConfigurationIdOrArn",
        configuration_set_name: "capo_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn.ConfigurationSetNameOrArn",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.associate_protect_configuration_result.AssociateProtectConfigurationResult":
        """<p>Associate a protect configuration with a configuration set. This replaces the configuration sets current protect configuration. A configuration set can only be associated with one protect configuration at a time. A protect configuration can be associated with multiple configuration sets.</p>

        Args:
            protect_configuration_id: <p>The unique identifier for the protect configuration.</p>
            configuration_set_name: <p>The name of the ConfigurationSet.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.associate_protect_configuration_request.AssociateProtectConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.associate_protect_configuration_result.AssociateProtectConfigurationResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.associate_protect_configuration

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.associate_protect_configuration.async_associate_protect_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.associate_protect_configuration_request.AssociateProtectConfigurationRequest = {
            "protect_configuration_id": protect_configuration_id,
            "configuration_set_name": configuration_set_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def carrier_lookup(
        self,
        phone_number: "capo_pinpoint_sms_voice_v2.types.carrier_lookup_input_phone_number_type.CarrierLookupInputPhoneNumberType",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        enable_cleansing: Optional[bool] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.carrier_lookup_result.CarrierLookupResult":
        """<p>Returns information about a destination phone number, including whether the number type and whether it is valid, the carrier, and more.</p>

        Args:
            phone_number: <p>The phone number that you want to retrieve information about. You can provide the phone number in various formats including special characters such as parentheses, brackets, spaces, hyphens, periods, and commas. The service automatically converts the input to E164 format for processing.</p>
            enable_cleansing: <p>Specifies whether the service cleanses the phone number that you provide. When set to <code>true</code>, the service normalizes the phone number according to the destination country's national numbering plan and dialing rules. The service returns the cleansed number in E.164 format in the <code>E164PhoneNumber</code> field and returns the number that you provided in the <code>OriginalPhoneNumber</code> field.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Use CarrierLookup
            Call the CarrierLookup operation to get information about a customer provided phone number, including if the number is valid. The service accepts phone numbers with various formatting characters and returns the number in E164 format.

            >>> await client.carrier_lookup(phone_number='+1 (555) 555-5333')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.carrier_lookup_request.CarrierLookupRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.carrier_lookup_result.CarrierLookupResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.carrier_lookup

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.carrier_lookup.async_carrier_lookup(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.carrier_lookup_request.CarrierLookupRequest = {
            "phone_number": phone_number
        }
        if enable_cleansing is not None:
            input_["enable_cleansing"] = enable_cleansing

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_configuration_set(
        self,
        configuration_set_name: "capo_pinpoint_sms_voice_v2.types.configuration_set_name.ConfigurationSetName",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        tags: Optional["capo_pinpoint_sms_voice_v2.types.tag_list.TagList"] = None,
        client_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.create_configuration_set_result.CreateConfigurationSetResult":
        """<p>Creates a new configuration set. After you create the configuration set, you can add one or more event destinations to it.</p> <p>A configuration set is a set of rules that you apply to the SMS and voice messages that you send.</p> <p>When you send a message, you can optionally specify a single configuration set.</p>

        Args:
            configuration_set_name: <p>The name to use for the new configuration set.</p>
            tags: <p>An array of key and value pair tags that's associated with the new configuration set. </p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.create_configuration_set_request.CreateConfigurationSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.create_configuration_set_result.CreateConfigurationSetResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.create_configuration_set

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.create_configuration_set.async_create_configuration_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.create_configuration_set_request.CreateConfigurationSetRequest = {
            "configuration_set_name": configuration_set_name
        }
        if tags is not None:
            input_["tags"] = tags
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

    async def create_event_destination(
        self,
        configuration_set_name: "capo_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn.ConfigurationSetNameOrArn",
        event_destination_name: "capo_pinpoint_sms_voice_v2.types.event_destination_name.EventDestinationName",
        matching_event_types: "capo_pinpoint_sms_voice_v2.types.event_type_list.EventTypeList",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        cloud_watch_logs_destination: Optional[
            "capo_pinpoint_sms_voice_v2.types.cloud_watch_logs_destination.CloudWatchLogsDestination"
        ] = None,
        kinesis_firehose_destination: Optional[
            "capo_pinpoint_sms_voice_v2.types.kinesis_firehose_destination.KinesisFirehoseDestination"
        ] = None,
        sns_destination: Optional[
            "capo_pinpoint_sms_voice_v2.types.sns_destination.SnsDestination"
        ] = None,
        client_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.create_event_destination_result.CreateEventDestinationResult":
        """<p>Creates a new event destination in a configuration set.</p> <p>An event destination is a location where you send message events. The event options are Amazon CloudWatch, Amazon Data Firehose, or Amazon SNS. For example, when a message is delivered successfully, you can send information about that event to an event destination, or send notifications to endpoints that are subscribed to an Amazon SNS topic. </p> <p>You can only create one event destination at a time. You must provide a value for a single event destination using either <code>CloudWatchLogsDestination</code>, <code>KinesisFirehoseDestination</code> or <code>SnsDestination</code>. If an event destination isn't provided then an exception is returned.</p> <p>Each configuration set can contain between 0 and 5 event destinations. Each event destination can contain a reference to a single destination, such as a CloudWatch or Firehose destination.</p>

        Args:
            configuration_set_name: <p>Either the name of the configuration set or the configuration set ARN to apply event logging to. The ConfigurateSetName and ConfigurationSetArn can be found using the <a>DescribeConfigurationSets</a> action.</p>
            event_destination_name: <p>The name that identifies the event destination.</p>
            matching_event_types: <p>An array of event types that determine which events to log. If "ALL" is used, then End User Messaging SMS logs every event type.</p> <note> <p>The <code>TEXT_SENT</code> event type is not supported.</p> </note>
            cloud_watch_logs_destination: <p>An object that contains information about an event destination for logging to Amazon CloudWatch Logs.</p>
            kinesis_firehose_destination: <p>An object that contains information about an event destination for logging to Amazon Data Firehose.</p>
            sns_destination: <p>An object that contains information about an event destination for logging to Amazon SNS.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.create_event_destination_request.CreateEventDestinationRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.create_event_destination_result.CreateEventDestinationResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.create_event_destination

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.create_event_destination.async_create_event_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.create_event_destination_request.CreateEventDestinationRequest = {
            "configuration_set_name": configuration_set_name,
            "event_destination_name": event_destination_name,
            "matching_event_types": matching_event_types,
        }
        if cloud_watch_logs_destination is not None:
            input_["cloud_watch_logs_destination"] = cloud_watch_logs_destination
        if kinesis_firehose_destination is not None:
            input_["kinesis_firehose_destination"] = kinesis_firehose_destination
        if sns_destination is not None:
            input_["sns_destination"] = sns_destination
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

    async def create_notify_configuration(
        self,
        display_name: "capo_pinpoint_sms_voice_v2.types.notify_configuration_display_name.NotifyConfigurationDisplayName",
        use_case: "capo_pinpoint_sms_voice_v2.types.notify_configuration_use_case.NotifyConfigurationUseCase",
        enabled_channels: "capo_pinpoint_sms_voice_v2.types.notify_enabled_channels_list.NotifyEnabledChannelsList",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        default_template_id: Optional[
            "capo_pinpoint_sms_voice_v2.types.notify_template_id.NotifyTemplateId"
        ] = None,
        pool_id: Optional[
            "capo_pinpoint_sms_voice_v2.types.pool_id_or_arn.PoolIdOrArn"
        ] = None,
        enabled_countries: Optional[
            "capo_pinpoint_sms_voice_v2.types.iso_country_code_list.IsoCountryCodeList"
        ] = None,
        deletion_protection_enabled: Optional[bool] = None,
        client_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_pinpoint_sms_voice_v2.types.tag_list.TagList"] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.create_notify_configuration_result.CreateNotifyConfigurationResult":
        """<p>Creates a new notify configuration for managed messaging. A notify configuration defines the settings for sending templated messages, including the display name, use case, enabled channels, and enabled countries.</p>

        Args:
            display_name: <p>The display name to associate with the notify configuration.</p>
            use_case: <p>The use case for the notify configuration.</p>
            default_template_id: <p>The default template identifier to associate with the notify configuration. If specified, this template is used when sending messages without an explicit template identifier.</p>
            pool_id: <p>The identifier of the pool to associate with the notify configuration.</p>
            enabled_countries: <p>An array of two-character ISO country codes, in ISO 3166-1 alpha-2 format, that are enabled for the notify configuration.</p>
            enabled_channels: <p>An array of channels to enable for the notify configuration. Supported values include <code>SMS</code> and <code>VOICE</code>.</p>
            deletion_protection_enabled: <p>By default this is set to false. When set to true the notify configuration can't be deleted. You can change this value using the <a>UpdateNotifyConfiguration</a> action.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>
            tags: <p>An array of tags (key and value pairs) associated with the notify configuration.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            CreateNotifyConfiguration
            Create a notify configuration for OTP code verification over SMS.

            >>> await client.create_notify_configuration(display_name='MyOTPConfig', use_case='CODE_VERIFICATION', enabled_channels=['SMS'], enabled_countries=['US', 'CA'], deletion_protection_enabled=False, tags=[{'Key': 'Environment', 'Value': 'Production'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.create_notify_configuration_request.CreateNotifyConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.create_notify_configuration_result.CreateNotifyConfigurationResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.create_notify_configuration

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.create_notify_configuration.async_create_notify_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.create_notify_configuration_request.CreateNotifyConfigurationRequest = {
            "display_name": display_name,
            "use_case": use_case,
            "enabled_channels": enabled_channels,
        }
        if default_template_id is not None:
            input_["default_template_id"] = default_template_id
        if pool_id is not None:
            input_["pool_id"] = pool_id
        if enabled_countries is not None:
            input_["enabled_countries"] = enabled_countries
        if deletion_protection_enabled is not None:
            input_["deletion_protection_enabled"] = deletion_protection_enabled
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

    async def create_opt_out_list(
        self,
        opt_out_list_name: "capo_pinpoint_sms_voice_v2.types.opt_out_list_name.OptOutListName",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        tags: Optional["capo_pinpoint_sms_voice_v2.types.tag_list.TagList"] = None,
        client_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.create_opt_out_list_result.CreateOptOutListResult":
        """<p>Creates a new opt-out list.</p> <p>If the opt-out list name already exists, an error is returned.</p> <p>An opt-out list is a list of phone numbers that are opted out, meaning you can't send SMS or voice messages to them. If end user replies with the keyword "STOP," an entry for the phone number is added to the opt-out list. In addition to STOP, your recipients can use any supported opt-out keyword, such as CANCEL or OPTOUT. For a list of supported opt-out keywords, see <a href="https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms-manage.html#channels-sms-manage-optout"> SMS opt out </a> in the End User Messaging SMS User Guide.</p>

        Args:
            opt_out_list_name: <p>The name of the new OptOutList.</p>
            tags: <p>An array of tags (key and value pairs) to associate with the new OptOutList.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.create_opt_out_list_request.CreateOptOutListRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.create_opt_out_list_result.CreateOptOutListResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.create_opt_out_list

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.create_opt_out_list.async_create_opt_out_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.create_opt_out_list_request.CreateOptOutListRequest = {
            "opt_out_list_name": opt_out_list_name
        }
        if tags is not None:
            input_["tags"] = tags
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

    async def create_pool(
        self,
        origination_identity: "capo_pinpoint_sms_voice_v2.types.phone_or_sender_id_or_arn.PhoneOrSenderIdOrArn",
        message_type: "capo_pinpoint_sms_voice_v2.types.message_type.MessageType",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        iso_country_code: Optional[
            "capo_pinpoint_sms_voice_v2.types.iso_country_code.IsoCountryCode"
        ] = None,
        deletion_protection_enabled: Optional[bool] = None,
        tags: Optional["capo_pinpoint_sms_voice_v2.types.tag_list.TagList"] = None,
        client_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.create_pool_result.CreatePoolResult":
        """<p>Creates a new pool and associates the specified origination identity to the pool. A pool can include one or more phone numbers and SenderIds that are associated with your Amazon Web Services account.</p> <p>The new pool inherits its configuration from the specified origination identity. This includes keywords, message type, opt-out list, two-way configuration, and self-managed opt-out configuration. Deletion protection isn't inherited from the origination identity and defaults to false.</p> <p>If the origination identity is a phone number and is already associated with another pool, an error is returned. A sender ID can be associated with multiple pools.</p>

        Args:
            origination_identity: <p>The origination identity to use such as a PhoneNumberId, PhoneNumberArn, SenderId or SenderIdArn. You can use <a href="https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribePhoneNumbers.html">DescribePhoneNumbers</a> to find the values for PhoneNumberId and PhoneNumberArn, and use <a href="https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeSenderIds.html">DescribeSenderIds</a> can be used to get the values for SenderId and SenderIdArn.</p> <p>After the pool is created you can add more origination identities to the pool by using <a href="https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_AssociateOriginationIdentity.html">AssociateOriginationIdentity</a>.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>
            iso_country_code: <p>The new two-character code, in ISO 3166-1 alpha-2 format, for the country or region of the new pool. This field is optional and is not required for origination identity types that are not country-specific, such as RCS agents.</p>
            message_type: <p>The type of message. Valid values are TRANSACTIONAL for messages that are critical or time-sensitive and PROMOTIONAL for messages that aren't critical or time-sensitive. After the pool is created the MessageType can't be changed.</p>
            deletion_protection_enabled: <p>By default this is set to false. When set to true the pool can't be deleted. You can change this value using the <a href="https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_UpdatePool.html">UpdatePool</a> action.</p>
            tags: <p>An array of tags (key and value pairs) associated with the pool.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.create_pool_request.CreatePoolRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.create_pool_result.CreatePoolResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.create_pool

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.create_pool.async_create_pool(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.create_pool_request.CreatePoolRequest = {
            "origination_identity": origination_identity,
            "message_type": message_type,
        }
        if iso_country_code is not None:
            input_["iso_country_code"] = iso_country_code
        if deletion_protection_enabled is not None:
            input_["deletion_protection_enabled"] = deletion_protection_enabled
        if tags is not None:
            input_["tags"] = tags
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

    async def create_protect_configuration(
        self,
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        client_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.client_token.ClientToken"
        ] = None,
        deletion_protection_enabled: Optional[bool] = None,
        tags: Optional["capo_pinpoint_sms_voice_v2.types.tag_list.TagList"] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.create_protect_configuration_result.CreateProtectConfigurationResult":
        """<p>Create a new protect configuration. By default all country rule sets for each capability are set to <code>ALLOW</code>. Update the country rule sets using <code>UpdateProtectConfigurationCountryRuleSet</code>. A protect configurations name is stored as a Tag with the key set to <code>Name</code> and value as the name of the protect configuration.</p>

        Args:
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>
            deletion_protection_enabled: <p>When set to true deletion protection is enabled. By default this is set to false. </p>
            tags: <p>An array of key and value pair tags that are associated with the resource.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.create_protect_configuration_request.CreateProtectConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.create_protect_configuration_result.CreateProtectConfigurationResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.create_protect_configuration

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.create_protect_configuration.async_create_protect_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.create_protect_configuration_request.CreateProtectConfigurationRequest = {}
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if deletion_protection_enabled is not None:
            input_["deletion_protection_enabled"] = deletion_protection_enabled
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_rcs_agent(
        self,
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        deletion_protection_enabled: Optional[bool] = None,
        opt_out_list_name: Optional[
            "capo_pinpoint_sms_voice_v2.types.opt_out_list_name_or_arn.OptOutListNameOrArn"
        ] = None,
        tags: Optional["capo_pinpoint_sms_voice_v2.types.tag_list.TagList"] = None,
        client_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.client_token.ClientToken"
        ] = None,
    ) -> (
        "capo_pinpoint_sms_voice_v2.types.create_rcs_agent_result.CreateRcsAgentResult"
    ):
        """<p>Creates a new RCS agent for sending rich messages through the RCS channel. The RCS agent serves as an origination identity for sending RCS messages to your recipients.</p>

        Args:
            deletion_protection_enabled: <p>By default this is set to false. When set to true the RCS agent can't be deleted. You can change this value using the <a>UpdateRcsAgent</a> action.</p>
            opt_out_list_name: <p>The OptOutList to associate with the RCS agent. Valid values are either OptOutListName or OptOutListArn.</p>
            tags: <p>An array of tags (key and value pairs) associated with the RCS agent.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.create_rcs_agent_request.CreateRcsAgentRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.create_rcs_agent_result.CreateRcsAgentResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.create_rcs_agent

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.create_rcs_agent.async_create_rcs_agent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.create_rcs_agent_request.CreateRcsAgentRequest = {}
        if deletion_protection_enabled is not None:
            input_["deletion_protection_enabled"] = deletion_protection_enabled
        if opt_out_list_name is not None:
            input_["opt_out_list_name"] = opt_out_list_name
        if tags is not None:
            input_["tags"] = tags
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

    async def create_registration(
        self,
        registration_type: "capo_pinpoint_sms_voice_v2.types.registration_type.RegistrationType",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        tags: Optional["capo_pinpoint_sms_voice_v2.types.tag_list.TagList"] = None,
        client_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.create_registration_result.CreateRegistrationResult":
        """<p>Creates a new registration based on the <b>RegistrationType</b> field. </p>

        Args:
            registration_type: <p>The type of registration form to create. The list of <b>RegistrationTypes</b> can be found using the <a>DescribeRegistrationTypeDefinitions</a> action.</p>
            tags: <p>An array of tags (key and value pairs) to associate with the registration.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.create_registration_request.CreateRegistrationRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.create_registration_result.CreateRegistrationResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.create_registration

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.create_registration.async_create_registration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.create_registration_request.CreateRegistrationRequest = {
            "registration_type": registration_type
        }
        if tags is not None:
            input_["tags"] = tags
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

    async def create_registration_association(
        self,
        registration_id: "capo_pinpoint_sms_voice_v2.types.registration_id_or_arn.RegistrationIdOrArn",
        resource_id: "capo_pinpoint_sms_voice_v2.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.create_registration_association_result.CreateRegistrationAssociationResult":
        """<p>Associate the registration with an origination identity such as a phone number or sender ID.</p>

        Args:
            registration_id: <p>The unique identifier for the registration.</p>
            resource_id: <p>The unique identifier for the origination identity. For example this could be a <b>PhoneNumberId</b> or <b>SenderId</b>.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.create_registration_association_request.CreateRegistrationAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.create_registration_association_result.CreateRegistrationAssociationResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.create_registration_association

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.create_registration_association.async_create_registration_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.create_registration_association_request.CreateRegistrationAssociationRequest = {
            "registration_id": registration_id,
            "resource_id": resource_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_registration_attachment(
        self,
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        attachment_body: Optional[
            "capo_pinpoint_sms_voice_v2.types.attachment_body.AttachmentBody"
        ] = None,
        attachment_url: Optional[
            "capo_pinpoint_sms_voice_v2.types.attachment_url.AttachmentUrl"
        ] = None,
        tags: Optional["capo_pinpoint_sms_voice_v2.types.tag_list.TagList"] = None,
        client_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.create_registration_attachment_result.CreateRegistrationAttachmentResult":
        """<p>Create a new registration attachment to use for uploading a file or a URL to a file. The maximum file size is 5MB and valid file extensions are PDF, JPEG and PNG. For example, many sender ID registrations require a signed “letter of authorization” (LOA) to be submitted.</p> <p>Use either <code>AttachmentUrl</code> or <code>AttachmentBody</code> to upload your attachment. If both are specified then an exception is returned.</p>

        Args:
            attachment_body: <p>The registration file to upload. The maximum file size is 5MB and valid file extensions are PDF, JPEG and PNG.</p>
            attachment_url: <p>Registration files have to be stored in an Amazon S3 bucket. The URI to use when sending is in the format <code>s3://BucketName/FileName</code>.</p>
            tags: <p>An array of tags (key and value pairs) to associate with the registration attachment.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.create_registration_attachment_request.CreateRegistrationAttachmentRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.create_registration_attachment_result.CreateRegistrationAttachmentResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.create_registration_attachment

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.create_registration_attachment.async_create_registration_attachment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.create_registration_attachment_request.CreateRegistrationAttachmentRequest = {}
        if attachment_body is not None:
            input_["attachment_body"] = attachment_body
        if attachment_url is not None:
            input_["attachment_url"] = attachment_url
        if tags is not None:
            input_["tags"] = tags
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

    async def create_registration_version(
        self,
        registration_id: "capo_pinpoint_sms_voice_v2.types.registration_id_or_arn.RegistrationIdOrArn",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.create_registration_version_result.CreateRegistrationVersionResult":
        """<p>Create a new version of the registration and increase the <b>VersionNumber</b>. The previous version of the registration becomes read-only.</p>

        Args:
            registration_id: <p>The unique identifier for the registration.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.create_registration_version_request.CreateRegistrationVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.create_registration_version_result.CreateRegistrationVersionResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.create_registration_version

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.create_registration_version.async_create_registration_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.create_registration_version_request.CreateRegistrationVersionRequest = {
            "registration_id": registration_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_verified_destination_number(
        self,
        destination_phone_number: "capo_pinpoint_sms_voice_v2.types.phone_number.PhoneNumber",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        rcs_agent_id: Optional[
            "capo_pinpoint_sms_voice_v2.types.rcs_agent_id_or_arn.RcsAgentIdOrArn"
        ] = None,
        tags: Optional["capo_pinpoint_sms_voice_v2.types.tag_list.TagList"] = None,
        client_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.create_verified_destination_number_result.CreateVerifiedDestinationNumberResult":
        """<p>You can only send messages to verified destination numbers when your account is in the sandbox. You can add up to 10 verified destination numbers.</p>

        Args:
            destination_phone_number: <p>The verified destination phone number, in E.164 format.</p>
            rcs_agent_id: <p>The unique identifier of the RCS agent to associate with the verified destination number. You can use either the RcsAgentId or RcsAgentArn.</p>
            tags: <p>An array of tags (key and value pairs) to associate with the destination number.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.create_verified_destination_number_request.CreateVerifiedDestinationNumberRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.create_verified_destination_number_result.CreateVerifiedDestinationNumberResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.create_verified_destination_number

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.create_verified_destination_number.async_create_verified_destination_number(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.create_verified_destination_number_request.CreateVerifiedDestinationNumberRequest = {
            "destination_phone_number": destination_phone_number
        }
        if rcs_agent_id is not None:
            input_["rcs_agent_id"] = rcs_agent_id
        if tags is not None:
            input_["tags"] = tags
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

    async def delete_account_default_protect_configuration(
        self, *, config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None
    ) -> "capo_pinpoint_sms_voice_v2.types.delete_account_default_protect_configuration_result.DeleteAccountDefaultProtectConfigurationResult":
        """<p>Removes the current account default protect configuration.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.delete_account_default_protect_configuration_request.DeleteAccountDefaultProtectConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.delete_account_default_protect_configuration_result.DeleteAccountDefaultProtectConfigurationResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_account_default_protect_configuration

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_account_default_protect_configuration.async_delete_account_default_protect_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.delete_account_default_protect_configuration_request.DeleteAccountDefaultProtectConfigurationRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_configuration_set(
        self,
        configuration_set_name: "capo_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn.ConfigurationSetNameOrArn",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.delete_configuration_set_result.DeleteConfigurationSetResult":
        """<p>Deletes an existing configuration set.</p> <p>A configuration set is a set of rules that you apply to voice and SMS messages that you send. In a configuration set, you can specify a destination for specific types of events related to voice and SMS messages. </p>

        Args:
            configuration_set_name: <p>The name of the configuration set or the configuration set ARN that you want to delete. The ConfigurationSetName and ConfigurationSetArn can be found using the <a>DescribeConfigurationSets</a> action.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.delete_configuration_set_request.DeleteConfigurationSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.delete_configuration_set_result.DeleteConfigurationSetResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_configuration_set

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_configuration_set.async_delete_configuration_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.delete_configuration_set_request.DeleteConfigurationSetRequest = {
            "configuration_set_name": configuration_set_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_default_message_type(
        self,
        configuration_set_name: "capo_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn.ConfigurationSetNameOrArn",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.delete_default_message_type_result.DeleteDefaultMessageTypeResult":
        """<p>Deletes an existing default message type on a configuration set.</p> <p> A message type is a type of messages that you plan to send. If you send account-related messages or time-sensitive messages such as one-time passcodes, choose <b>Transactional</b>. If you plan to send messages that contain marketing material or other promotional content, choose <b>Promotional</b>. This setting applies to your entire Amazon Web Services account. </p>

        Args:
            configuration_set_name: <p>The name of the configuration set or the configuration set Amazon Resource Name (ARN) to delete the default message type from. The ConfigurationSetName and ConfigurationSetArn can be found using the <a>DescribeConfigurationSets</a> action.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.delete_default_message_type_request.DeleteDefaultMessageTypeRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.delete_default_message_type_result.DeleteDefaultMessageTypeResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_default_message_type

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_default_message_type.async_delete_default_message_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.delete_default_message_type_request.DeleteDefaultMessageTypeRequest = {
            "configuration_set_name": configuration_set_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_default_sender_id(
        self,
        configuration_set_name: "capo_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn.ConfigurationSetNameOrArn",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.delete_default_sender_id_result.DeleteDefaultSenderIdResult":
        """<p>Deletes an existing default sender ID on a configuration set.</p> <p>A default sender ID is the identity that appears on recipients' devices when they receive SMS messages. Support for sender ID capabilities varies by country or region.</p>

        Args:
            configuration_set_name: <p>The name of the configuration set or the configuration set Amazon Resource Name (ARN) to delete the default sender ID from. The ConfigurationSetName and ConfigurationSetArn can be found using the <a>DescribeConfigurationSets</a> action.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.delete_default_sender_id_request.DeleteDefaultSenderIdRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.delete_default_sender_id_result.DeleteDefaultSenderIdResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_default_sender_id

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_default_sender_id.async_delete_default_sender_id(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.delete_default_sender_id_request.DeleteDefaultSenderIdRequest = {
            "configuration_set_name": configuration_set_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_event_destination(
        self,
        configuration_set_name: "capo_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn.ConfigurationSetNameOrArn",
        event_destination_name: "capo_pinpoint_sms_voice_v2.types.event_destination_name.EventDestinationName",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.delete_event_destination_result.DeleteEventDestinationResult":
        """<p>Deletes an existing event destination.</p> <p>An event destination is a location where you send response information about the messages that you send. For example, when a message is delivered successfully, you can send information about that event to an Amazon CloudWatch destination, or send notifications to endpoints that are subscribed to an Amazon SNS topic.</p>

        Args:
            configuration_set_name: <p>The name of the configuration set or the configuration set's Amazon Resource Name (ARN) to remove the event destination from. The ConfigurateSetName and ConfigurationSetArn can be found using the <a>DescribeConfigurationSets</a> action.</p>
            event_destination_name: <p>The name of the event destination to delete.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.delete_event_destination_request.DeleteEventDestinationRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.delete_event_destination_result.DeleteEventDestinationResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_event_destination

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_event_destination.async_delete_event_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.delete_event_destination_request.DeleteEventDestinationRequest = {
            "configuration_set_name": configuration_set_name,
            "event_destination_name": event_destination_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_keyword(
        self,
        origination_identity: "capo_pinpoint_sms_voice_v2.types.phone_or_pool_id_or_arn.PhoneOrPoolIdOrArn",
        keyword: "capo_pinpoint_sms_voice_v2.types.keyword.Keyword",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.delete_keyword_result.DeleteKeywordResult":
        """<p>Deletes an existing keyword from an origination phone number or pool.</p> <p>A keyword is a word that you can search for on a particular phone number or pool. It is also a specific word or phrase that an end user can send to your number to elicit a response, such as an informational message or a special offer. When your number receives a message that begins with a keyword, End User Messaging SMS responds with a customizable message.</p> <p>Keywords "HELP" and "STOP" can't be deleted or modified.</p>

        Args:
            origination_identity: <p>The origination identity to use such as a PhoneNumberId, PhoneNumberArn, PoolId or PoolArn. You can use <a>DescribePhoneNumbers</a> to find the values for PhoneNumberId and PhoneNumberArn and <a>DescribePools</a> to find the values of PoolId and PoolArn.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>
            keyword: <p>The keyword to delete.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.delete_keyword_request.DeleteKeywordRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.delete_keyword_result.DeleteKeywordResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_keyword

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_keyword.async_delete_keyword(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.delete_keyword_request.DeleteKeywordRequest = {
            "origination_identity": origination_identity,
            "keyword": keyword,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_media_message_spend_limit_override(
        self, *, config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None
    ) -> "capo_pinpoint_sms_voice_v2.types.delete_media_message_spend_limit_override_result.DeleteMediaMessageSpendLimitOverrideResult":
        """<p>Deletes an account-level monthly spending limit override for sending multimedia messages (MMS). Deleting a spend limit override will set the <code>EnforcedLimit</code> to equal the <code>MaxLimit</code>, which is controlled by Amazon Web Services. For more information on spend limits (quotas) see <a href="https://docs.aws.amazon.com/sms-voice/latest/userguide/quotas.html">Quotas for Server Migration Service</a> in the <i>Server Migration Service User Guide</i>.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.delete_media_message_spend_limit_override_request.DeleteMediaMessageSpendLimitOverrideRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.delete_media_message_spend_limit_override_result.DeleteMediaMessageSpendLimitOverrideResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_media_message_spend_limit_override

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_media_message_spend_limit_override.async_delete_media_message_spend_limit_override(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.delete_media_message_spend_limit_override_request.DeleteMediaMessageSpendLimitOverrideRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_notify_configuration(
        self,
        notify_configuration_id: "capo_pinpoint_sms_voice_v2.types.notify_configuration_id_or_arn.NotifyConfigurationIdOrArn",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.delete_notify_configuration_result.DeleteNotifyConfigurationResult":
        """<p>Deletes an existing notify configuration.</p> <p>If deletion protection is enabled, an error is returned.</p>

        Args:
            notify_configuration_id: <p>The identifier of the notify configuration to delete. The NotifyConfigurationId can be found using the <a>DescribeNotifyConfigurations</a> operation.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DeleteNotifyConfiguration
            Delete an existing notify configuration.

            >>> await client.delete_notify_configuration(notify_configuration_id='nc-1234567890abcdef0')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.delete_notify_configuration_request.DeleteNotifyConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.delete_notify_configuration_result.DeleteNotifyConfigurationResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_notify_configuration

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_notify_configuration.async_delete_notify_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.delete_notify_configuration_request.DeleteNotifyConfigurationRequest = {
            "notify_configuration_id": notify_configuration_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_notify_message_spend_limit_override(
        self, *, config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None
    ) -> "capo_pinpoint_sms_voice_v2.types.delete_notify_message_spend_limit_override_result.DeleteNotifyMessageSpendLimitOverrideResult":
        """<p>Deletes an account-level monthly spending limit override for sending notify messages. Deleting a spend limit override will set the <code>EnforcedLimit</code> to equal the <code>MaxLimit</code>, which is controlled by Amazon Web Services. For more information on spend limits (quotas) see <a href="https://docs.aws.amazon.com/sms-voice/latest/userguide/quotas.html">Quotas </a> in the <i>End User Messaging SMS User Guide</i>.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DeleteNotifyMessageSpendLimitOverride
            Delete the monthly spend limit override for notify messages, reverting to the default limit.

            >>> await client.delete_notify_message_spend_limit_override()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.delete_notify_message_spend_limit_override_request.DeleteNotifyMessageSpendLimitOverrideRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.delete_notify_message_spend_limit_override_result.DeleteNotifyMessageSpendLimitOverrideResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_notify_message_spend_limit_override

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_notify_message_spend_limit_override.async_delete_notify_message_spend_limit_override(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.delete_notify_message_spend_limit_override_request.DeleteNotifyMessageSpendLimitOverrideRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_opted_out_number(
        self,
        opt_out_list_name: "capo_pinpoint_sms_voice_v2.types.opt_out_list_name_or_arn.OptOutListNameOrArn",
        opted_out_number: "capo_pinpoint_sms_voice_v2.types.phone_number.PhoneNumber",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.delete_opted_out_number_result.DeleteOptedOutNumberResult":
        """<p>Deletes an existing opted out destination phone number from the specified opt-out list.</p> <p>Each destination phone number can only be deleted once every 30 days.</p> <p>If the specified destination phone number doesn't exist or if the opt-out list doesn't exist, an error is returned.</p>

        Args:
            opt_out_list_name: <p>The OptOutListName or OptOutListArn to remove the phone number from.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>
            opted_out_number: <p>The phone number, in E.164 format, to remove from the OptOutList.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.delete_opted_out_number_request.DeleteOptedOutNumberRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.delete_opted_out_number_result.DeleteOptedOutNumberResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_opted_out_number

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_opted_out_number.async_delete_opted_out_number(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.delete_opted_out_number_request.DeleteOptedOutNumberRequest = {
            "opt_out_list_name": opt_out_list_name,
            "opted_out_number": opted_out_number,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_opt_out_list(
        self,
        opt_out_list_name: "capo_pinpoint_sms_voice_v2.types.opt_out_list_name_or_arn.OptOutListNameOrArn",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.delete_opt_out_list_result.DeleteOptOutListResult":
        """<p>Deletes an existing opt-out list. All opted out phone numbers in the opt-out list are deleted.</p> <p>If the specified opt-out list name doesn't exist or is in-use by an origination phone number or pool, an error is returned.</p>

        Args:
            opt_out_list_name: <p>The OptOutListName or OptOutListArn of the OptOutList to delete. You can use <a>DescribeOptOutLists</a> to find the values for OptOutListName and OptOutListArn.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.delete_opt_out_list_request.DeleteOptOutListRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.delete_opt_out_list_result.DeleteOptOutListResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_opt_out_list

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_opt_out_list.async_delete_opt_out_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.delete_opt_out_list_request.DeleteOptOutListRequest = {
            "opt_out_list_name": opt_out_list_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_pool(
        self,
        pool_id: "capo_pinpoint_sms_voice_v2.types.pool_id_or_arn.PoolIdOrArn",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.delete_pool_result.DeletePoolResult":
        """<p>Deletes an existing pool. Deleting a pool disassociates all origination identities from that pool.</p> <p>If the pool status isn't active or if deletion protection is enabled, an error is returned.</p> <p>A pool is a collection of phone numbers and SenderIds. A pool can include one or more phone numbers and SenderIds that are associated with your Amazon Web Services account.</p>

        Args:
            pool_id: <p>The PoolId or PoolArn of the pool to delete. You can use <a>DescribePools</a> to find the values for PoolId and PoolArn .</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.delete_pool_request.DeletePoolRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.delete_pool_result.DeletePoolResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_pool

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_pool.async_delete_pool(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.delete_pool_request.DeletePoolRequest = {
            "pool_id": pool_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_protect_configuration(
        self,
        protect_configuration_id: "capo_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn.ProtectConfigurationIdOrArn",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.delete_protect_configuration_result.DeleteProtectConfigurationResult":
        """<p>Permanently delete the protect configuration. The protect configuration must have deletion protection disabled and must not be associated as the account default protect configuration or associated with a configuration set.</p>

        Args:
            protect_configuration_id: <p>The unique identifier for the protect configuration.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.delete_protect_configuration_request.DeleteProtectConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.delete_protect_configuration_result.DeleteProtectConfigurationResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_protect_configuration

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_protect_configuration.async_delete_protect_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.delete_protect_configuration_request.DeleteProtectConfigurationRequest = {
            "protect_configuration_id": protect_configuration_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_protect_configuration_rule_set_number_override(
        self,
        protect_configuration_id: "capo_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn.ProtectConfigurationIdOrArn",
        destination_phone_number: "capo_pinpoint_sms_voice_v2.types.phone_number.PhoneNumber",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.delete_protect_configuration_rule_set_number_override_result.DeleteProtectConfigurationRuleSetNumberOverrideResult":
        """<p>Permanently delete the protect configuration rule set number override.</p>

        Args:
            protect_configuration_id: <p>The unique identifier for the protect configuration.</p>
            destination_phone_number: <p>The destination phone number in E.164 format.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.delete_protect_configuration_rule_set_number_override_request.DeleteProtectConfigurationRuleSetNumberOverrideRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.delete_protect_configuration_rule_set_number_override_result.DeleteProtectConfigurationRuleSetNumberOverrideResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_protect_configuration_rule_set_number_override

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_protect_configuration_rule_set_number_override.async_delete_protect_configuration_rule_set_number_override(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.delete_protect_configuration_rule_set_number_override_request.DeleteProtectConfigurationRuleSetNumberOverrideRequest = {
            "protect_configuration_id": protect_configuration_id,
            "destination_phone_number": destination_phone_number,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_rcs_agent(
        self,
        rcs_agent_id: "capo_pinpoint_sms_voice_v2.types.rcs_agent_id_or_arn.RcsAgentIdOrArn",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> (
        "capo_pinpoint_sms_voice_v2.types.delete_rcs_agent_result.DeleteRcsAgentResult"
    ):
        """<p>Deletes an existing RCS agent. If deletion protection is enabled, an error is returned.</p>

        Args:
            rcs_agent_id: <p>The unique identifier of the RCS agent to delete. You can use either the RcsAgentId or RcsAgentArn.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.delete_rcs_agent_request.DeleteRcsAgentRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.delete_rcs_agent_result.DeleteRcsAgentResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_rcs_agent

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_rcs_agent.async_delete_rcs_agent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.delete_rcs_agent_request.DeleteRcsAgentRequest = {
            "rcs_agent_id": rcs_agent_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_rcs_message_spend_limit_override(
        self, *, config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None
    ) -> "capo_pinpoint_sms_voice_v2.types.delete_rcs_message_spend_limit_override_result.DeleteRcsMessageSpendLimitOverrideResult":
        """<p>Deletes an account-level monthly spending limit override for sending RCS messages. Deleting a spend limit override sets the <code>EnforcedLimit</code> to equal the <code>MaxLimit</code>, which is set by Amazon Web Services.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.delete_rcs_message_spend_limit_override_request.DeleteRcsMessageSpendLimitOverrideRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.delete_rcs_message_spend_limit_override_result.DeleteRcsMessageSpendLimitOverrideResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_rcs_message_spend_limit_override

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_rcs_message_spend_limit_override.async_delete_rcs_message_spend_limit_override(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.delete_rcs_message_spend_limit_override_request.DeleteRcsMessageSpendLimitOverrideRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_registration(
        self,
        registration_id: "capo_pinpoint_sms_voice_v2.types.registration_id_or_arn.RegistrationIdOrArn",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.delete_registration_result.DeleteRegistrationResult":
        """<p>Permanently delete an existing registration from your account.</p>

        Args:
            registration_id: <p>The unique identifier for the registration.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.delete_registration_request.DeleteRegistrationRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.delete_registration_result.DeleteRegistrationResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_registration

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_registration.async_delete_registration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.delete_registration_request.DeleteRegistrationRequest = {
            "registration_id": registration_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_registration_attachment(
        self,
        registration_attachment_id: "capo_pinpoint_sms_voice_v2.types.registration_attachment_id_or_arn.RegistrationAttachmentIdOrArn",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.delete_registration_attachment_result.DeleteRegistrationAttachmentResult":
        """<p>Permanently delete the specified registration attachment.</p>

        Args:
            registration_attachment_id: <p>The unique identifier for the registration attachment.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.delete_registration_attachment_request.DeleteRegistrationAttachmentRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.delete_registration_attachment_result.DeleteRegistrationAttachmentResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_registration_attachment

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_registration_attachment.async_delete_registration_attachment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.delete_registration_attachment_request.DeleteRegistrationAttachmentRequest = {
            "registration_attachment_id": registration_attachment_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_registration_field_value(
        self,
        registration_id: "capo_pinpoint_sms_voice_v2.types.registration_id_or_arn.RegistrationIdOrArn",
        field_path: "capo_pinpoint_sms_voice_v2.types.field_path.FieldPath",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.delete_registration_field_value_result.DeleteRegistrationFieldValueResult":
        """<p>Delete the value in a registration form field.</p>

        Args:
            registration_id: <p>The unique identifier for the registration.</p>
            field_path: <p>The path to the registration form field. You can use <a>DescribeRegistrationFieldDefinitions</a> for a list of <b>FieldPaths</b>.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.delete_registration_field_value_request.DeleteRegistrationFieldValueRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.delete_registration_field_value_result.DeleteRegistrationFieldValueResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_registration_field_value

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_registration_field_value.async_delete_registration_field_value(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.delete_registration_field_value_request.DeleteRegistrationFieldValueRequest = {
            "registration_id": registration_id,
            "field_path": field_path,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_resource_policy(
        self,
        resource_arn: "capo_pinpoint_sms_voice_v2.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.delete_resource_policy_result.DeleteResourcePolicyResult":
        """<p>Deletes the resource-based policy document attached to the End User Messaging SMS resource. A shared resource can be a Pool, Opt-out list, Sender Id, or Phone number.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the End User Messaging SMS resource you're deleting the resource-based policy from.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.delete_resource_policy_result.DeleteResourcePolicyResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_resource_policy

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_resource_policy.async_delete_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_text_message_spend_limit_override(
        self, *, config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None
    ) -> "capo_pinpoint_sms_voice_v2.types.delete_text_message_spend_limit_override_result.DeleteTextMessageSpendLimitOverrideResult":
        """<p>Deletes an account-level monthly spending limit override for sending text messages. Deleting a spend limit override will set the <code>EnforcedLimit</code> to equal the <code>MaxLimit</code>, which is controlled by Amazon Web Services. For more information on spend limits (quotas) see <a href="https://docs.aws.amazon.com/sms-voice/latest/userguide/quotas.html">Quotas </a> in the <i>End User Messaging SMS User Guide</i>.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.delete_text_message_spend_limit_override_request.DeleteTextMessageSpendLimitOverrideRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.delete_text_message_spend_limit_override_result.DeleteTextMessageSpendLimitOverrideResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_text_message_spend_limit_override

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_text_message_spend_limit_override.async_delete_text_message_spend_limit_override(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.delete_text_message_spend_limit_override_request.DeleteTextMessageSpendLimitOverrideRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_verified_destination_number(
        self,
        verified_destination_number_id: "capo_pinpoint_sms_voice_v2.types.verified_destination_number_id_or_arn.VerifiedDestinationNumberIdOrArn",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.delete_verified_destination_number_result.DeleteVerifiedDestinationNumberResult":
        """<p>Delete a verified destination phone number.</p>

        Args:
            verified_destination_number_id: <p>The unique identifier for the verified destination phone number.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.delete_verified_destination_number_request.DeleteVerifiedDestinationNumberRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.delete_verified_destination_number_result.DeleteVerifiedDestinationNumberResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_verified_destination_number

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_verified_destination_number.async_delete_verified_destination_number(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.delete_verified_destination_number_request.DeleteVerifiedDestinationNumberRequest = {
            "verified_destination_number_id": verified_destination_number_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_voice_message_spend_limit_override(
        self, *, config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None
    ) -> "capo_pinpoint_sms_voice_v2.types.delete_voice_message_spend_limit_override_result.DeleteVoiceMessageSpendLimitOverrideResult":
        """<p>Deletes an account level monthly spend limit override for sending voice messages. Deleting a spend limit override sets the <code>EnforcedLimit</code> equal to the <code>MaxLimit</code>, which is controlled by Amazon Web Services. For more information on spending limits (quotas) see <a href="https://docs.aws.amazon.com/sms-voice/latest/userguide/quotas.html">Quotas </a> in the <i>End User Messaging SMS User Guide</i>.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.delete_voice_message_spend_limit_override_request.DeleteVoiceMessageSpendLimitOverrideRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.delete_voice_message_spend_limit_override_result.DeleteVoiceMessageSpendLimitOverrideResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_voice_message_spend_limit_override

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.delete_voice_message_spend_limit_override.async_delete_voice_message_spend_limit_override(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.delete_voice_message_spend_limit_override_request.DeleteVoiceMessageSpendLimitOverrideRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_account_attributes(
        self,
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        next_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_pinpoint_sms_voice_v2.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.describe_account_attributes_result.DescribeAccountAttributesResult":
        """<p>Describes attributes of your Amazon Web Services account. The supported account attributes include account tier, which indicates whether your account is in the sandbox or production environment. When you're ready to move your account out of the sandbox, create an Amazon Web Services Support case for a service limit increase request.</p> <p>New accounts are placed into an SMS or voice sandbox. The sandbox protects both Amazon Web Services end recipients and SMS or voice recipients from fraud and abuse. </p>

        Args:
            next_token: <p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>
            max_results: <p>The maximum number of results to return per each request.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.describe_account_attributes_request.DescribeAccountAttributesRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.describe_account_attributes_result.DescribeAccountAttributesResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_account_attributes

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_account_attributes.async_describe_account_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.describe_account_attributes_request.DescribeAccountAttributesRequest = {}
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

    async def describe_account_limits(
        self,
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        next_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_pinpoint_sms_voice_v2.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.describe_account_limits_result.DescribeAccountLimitsResult":
        """<p>Describes the current End User Messaging SMS SMS Voice V2 resource quotas for your account. The description for a quota includes the quota name, current usage toward that quota, and the quota's maximum value.</p> <p>When you establish an Amazon Web Services account, the account has initial quotas on the maximum number of configuration sets, opt-out lists, phone numbers, and pools that you can create in a given Region. For more information see <a href="https://docs.aws.amazon.com/sms-voice/latest/userguide/quotas.html">Quotas </a> in the <i>End User Messaging SMS User Guide</i>.</p>

        Args:
            next_token: <p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>
            max_results: <p>The maximum number of results to return per each request.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.describe_account_limits_request.DescribeAccountLimitsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.describe_account_limits_result.DescribeAccountLimitsResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_account_limits

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_account_limits.async_describe_account_limits(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.describe_account_limits_request.DescribeAccountLimitsRequest = {}
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

    async def describe_configuration_sets(
        self,
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        configuration_set_names: Optional[
            "capo_pinpoint_sms_voice_v2.types.configuration_set_name_list.ConfigurationSetNameList"
        ] = None,
        filters: Optional[
            "capo_pinpoint_sms_voice_v2.types.configuration_set_filter_list.ConfigurationSetFilterList"
        ] = None,
        next_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_pinpoint_sms_voice_v2.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.describe_configuration_sets_result.DescribeConfigurationSetsResult":
        """<p>Describes the specified configuration sets or all in your account.</p> <p>If you specify configuration set names, the output includes information for only the specified configuration sets. If you specify filters, the output includes information for only those configuration sets that meet the filter criteria. If you don't specify configuration set names or filters, the output includes information for all configuration sets.</p> <p>If you specify a configuration set name that isn't valid, an error is returned.</p>

        Args:
            configuration_set_names: <p>An array of strings. Each element can be either a ConfigurationSetName or ConfigurationSetArn.</p>
            filters: <p>An array of filters to apply to the results that are returned.</p>
            next_token: <p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>
            max_results: <p>The maximum number of results to return per each request.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.describe_configuration_sets_request.DescribeConfigurationSetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.describe_configuration_sets_result.DescribeConfigurationSetsResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_configuration_sets

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_configuration_sets.async_describe_configuration_sets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.describe_configuration_sets_request.DescribeConfigurationSetsRequest = {}
        if configuration_set_names is not None:
            input_["configuration_set_names"] = configuration_set_names
        if filters is not None:
            input_["filters"] = filters
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

    async def describe_keywords(
        self,
        origination_identity: "capo_pinpoint_sms_voice_v2.types.phone_or_pool_id_or_arn.PhoneOrPoolIdOrArn",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        keywords: Optional[
            "capo_pinpoint_sms_voice_v2.types.keyword_list.KeywordList"
        ] = None,
        filters: Optional[
            "capo_pinpoint_sms_voice_v2.types.keyword_filter_list.KeywordFilterList"
        ] = None,
        next_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_pinpoint_sms_voice_v2.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.describe_keywords_result.DescribeKeywordsResult":
        """<p>Describes the specified keywords or all keywords on your origination phone number or pool.</p> <p>A keyword is a word that you can search for on a particular phone number or pool. It is also a specific word or phrase that an end user can send to your number to elicit a response, such as an informational message or a special offer. When your number receives a message that begins with a keyword, End User Messaging SMS responds with a customizable message.</p> <p>If you specify a keyword that isn't valid, an error is returned.</p>

        Args:
            origination_identity: <p>The origination identity to use such as a PhoneNumberId, PhoneNumberArn, SenderId or SenderIdArn. You can use <a>DescribePhoneNumbers</a> to find the values for PhoneNumberId and PhoneNumberArn while <a>DescribeSenderIds</a> can be used to get the values for SenderId and SenderIdArn.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>
            keywords: <p>An array of keywords to search for.</p>
            filters: <p>An array of keyword filters to filter the results.</p>
            next_token: <p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>
            max_results: <p>The maximum number of results to return per each request.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.describe_keywords_request.DescribeKeywordsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.describe_keywords_result.DescribeKeywordsResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_keywords

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_keywords.async_describe_keywords(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.describe_keywords_request.DescribeKeywordsRequest = {
            "origination_identity": origination_identity
        }
        if keywords is not None:
            input_["keywords"] = keywords
        if filters is not None:
            input_["filters"] = filters
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

    async def describe_notify_configurations(
        self,
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        notify_configuration_ids: Optional[
            "capo_pinpoint_sms_voice_v2.types.notify_configuration_id_list.NotifyConfigurationIdList"
        ] = None,
        filters: Optional[
            "capo_pinpoint_sms_voice_v2.types.notify_configuration_filter_list.NotifyConfigurationFilterList"
        ] = None,
        next_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_pinpoint_sms_voice_v2.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.describe_notify_configurations_result.DescribeNotifyConfigurationsResult":
        """<p>Describes the specified notify configurations or all notify configurations in your account.</p> <p>If you specify notify configuration IDs, the output includes information for only the specified notify configurations. If you specify filters, the output includes information for only those notify configurations that meet the filter criteria. If you don't specify notify configuration IDs or filters, the output includes information for all notify configurations.</p> <p>If you specify a notify configuration ID that isn't valid, an error is returned.</p>

        Args:
            notify_configuration_ids: <p>An array of notify configuration IDs to describe.</p>
            filters: <p>An array of NotifyConfigurationFilter objects to filter the results on.</p>
            next_token: <p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>
            max_results: <p>The maximum number of results to return per each request.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DescribeNotifyConfigurations
            Describe notify configurations filtered by status.

            >>> await client.describe_notify_configurations(filters=[{'Name': 'status', 'Values': ['ACTIVE']}], max_results=10)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.describe_notify_configurations_request.DescribeNotifyConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.describe_notify_configurations_result.DescribeNotifyConfigurationsResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_notify_configurations

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_notify_configurations.async_describe_notify_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.describe_notify_configurations_request.DescribeNotifyConfigurationsRequest = {}
        if notify_configuration_ids is not None:
            input_["notify_configuration_ids"] = notify_configuration_ids
        if filters is not None:
            input_["filters"] = filters
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

    async def describe_notify_templates(
        self,
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        template_ids: Optional[
            "capo_pinpoint_sms_voice_v2.types.notify_template_id_list.NotifyTemplateIdList"
        ] = None,
        filters: Optional[
            "capo_pinpoint_sms_voice_v2.types.notify_template_filter_list.NotifyTemplateFilterList"
        ] = None,
        next_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_pinpoint_sms_voice_v2.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.describe_notify_templates_result.DescribeNotifyTemplatesResult":
        """<p>Describes the specified notify templates or all notify templates in your account.</p> <p>If you specify template IDs, the output includes information for only the specified notify templates. If you specify filters, the output includes information for only those notify templates that meet the filter criteria. If you don't specify template IDs or filters, the output includes information for all notify templates.</p> <p>If you specify a template ID that isn't valid, an error is returned.</p>

        Args:
            template_ids: <p>An array of template IDs to describe.</p>
            filters: <p>An array of NotifyTemplateFilter objects to filter the results on.</p>
            next_token: <p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>
            max_results: <p>The maximum number of results to return per each request.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DescribeNotifyTemplates
            Describe available notify templates for OTP verification over SMS.

            >>> await client.describe_notify_templates(filters=[{'Name': 'template-type', 'Values': ['OTP_VERIFICATION']}, {'Name': 'channels', 'Values': ['SMS']}], max_results=10)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.describe_notify_templates_request.DescribeNotifyTemplatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.describe_notify_templates_result.DescribeNotifyTemplatesResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_notify_templates

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_notify_templates.async_describe_notify_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.describe_notify_templates_request.DescribeNotifyTemplatesRequest = {}
        if template_ids is not None:
            input_["template_ids"] = template_ids
        if filters is not None:
            input_["filters"] = filters
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

    async def describe_opted_out_numbers(
        self,
        opt_out_list_name: "capo_pinpoint_sms_voice_v2.types.opt_out_list_name_or_arn.OptOutListNameOrArn",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        opted_out_numbers: Optional[
            "capo_pinpoint_sms_voice_v2.types.opted_out_number_list.OptedOutNumberList"
        ] = None,
        filters: Optional[
            "capo_pinpoint_sms_voice_v2.types.opted_out_filter_list.OptedOutFilterList"
        ] = None,
        next_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_pinpoint_sms_voice_v2.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.describe_opted_out_numbers_result.DescribeOptedOutNumbersResult":
        """<p>Describes the specified opted out destination numbers or all opted out destination numbers in an opt-out list.</p> <p>If you specify opted out numbers, the output includes information for only the specified opted out numbers. If you specify filters, the output includes information for only those opted out numbers that meet the filter criteria. If you don't specify opted out numbers or filters, the output includes information for all opted out destination numbers in your opt-out list.</p> <p>If you specify an opted out number that isn't valid, an exception is returned.</p>

        Args:
            opt_out_list_name: <p>The OptOutListName or OptOutListArn of the OptOutList. You can use <a>DescribeOptOutLists</a> to find the values for OptOutListName and OptOutListArn.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>
            opted_out_numbers: <p>An array of phone numbers to search for in the OptOutList.</p> <p>If you specify an opted out number that isn't valid, an exception is returned.</p>
            filters: <p>An array of OptedOutFilter objects to filter the results on.</p>
            next_token: <p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>
            max_results: <p>The maximum number of results to return per each request.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.describe_opted_out_numbers_request.DescribeOptedOutNumbersRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.describe_opted_out_numbers_result.DescribeOptedOutNumbersResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_opted_out_numbers

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_opted_out_numbers.async_describe_opted_out_numbers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.describe_opted_out_numbers_request.DescribeOptedOutNumbersRequest = {
            "opt_out_list_name": opt_out_list_name
        }
        if opted_out_numbers is not None:
            input_["opted_out_numbers"] = opted_out_numbers
        if filters is not None:
            input_["filters"] = filters
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

    async def describe_opt_out_lists(
        self,
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        opt_out_list_names: Optional[
            "capo_pinpoint_sms_voice_v2.types.opt_out_list_name_list.OptOutListNameList"
        ] = None,
        next_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_pinpoint_sms_voice_v2.types.max_results.MaxResults"
        ] = None,
        owner: Optional["capo_pinpoint_sms_voice_v2.types.owner.Owner"] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.describe_opt_out_lists_result.DescribeOptOutListsResult":
        """<p>Describes the specified opt-out list or all opt-out lists in your account.</p> <p>If you specify opt-out list names, the output includes information for only the specified opt-out lists. Opt-out lists include only those that meet the filter criteria. If you don't specify opt-out list names or filters, the output includes information for all opt-out lists.</p> <p>If you specify an opt-out list name that isn't valid, an error is returned.</p>

        Args:
            opt_out_list_names: <p>The OptOutLists to show the details of. This is an array of strings that can be either the OptOutListName or OptOutListArn.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>
            next_token: <p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>
            max_results: <p>The maximum number of results to return per each request.</p>
            owner: <p>Use <code>SELF</code> to filter the list of Opt-Out List to ones your account owns or use <code>SHARED</code> to filter on Opt-Out List shared with your account. The <code>Owner</code> and <code>OptOutListNames</code> parameters can't be used at the same time.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.describe_opt_out_lists_request.DescribeOptOutListsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.describe_opt_out_lists_result.DescribeOptOutListsResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_opt_out_lists

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_opt_out_lists.async_describe_opt_out_lists(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.describe_opt_out_lists_request.DescribeOptOutListsRequest = {}
        if opt_out_list_names is not None:
            input_["opt_out_list_names"] = opt_out_list_names
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if owner is not None:
            input_["owner"] = owner

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_phone_numbers(
        self,
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        phone_number_ids: Optional[
            "capo_pinpoint_sms_voice_v2.types.phone_number_id_list.PhoneNumberIdList"
        ] = None,
        filters: Optional[
            "capo_pinpoint_sms_voice_v2.types.phone_number_filter_list.PhoneNumberFilterList"
        ] = None,
        next_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_pinpoint_sms_voice_v2.types.max_results.MaxResults"
        ] = None,
        owner: Optional["capo_pinpoint_sms_voice_v2.types.owner.Owner"] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.describe_phone_numbers_result.DescribePhoneNumbersResult":
        """<p>Describes the specified origination phone number, or all the phone numbers in your account.</p> <p>If you specify phone number IDs, the output includes information for only the specified phone numbers. If you specify filters, the output includes information for only those phone numbers that meet the filter criteria. If you don't specify phone number IDs or filters, the output includes information for all phone numbers.</p> <p>If you specify a phone number ID that isn't valid, an error is returned.</p>

        Args:
            phone_number_ids: <p>The unique identifier of phone numbers to find information about. This is an array of strings that can be either the PhoneNumberId or PhoneNumberArn.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>
            filters: <p>An array of PhoneNumberFilter objects to filter the results.</p>
            next_token: <p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>
            max_results: <p>The maximum number of results to return per each request.</p>
            owner: <p>Use <code>SELF</code> to filter the list of phone numbers to ones your account owns or use <code>SHARED</code> to filter on phone numbers shared with your account. The <code>Owner</code> and <code>PhoneNumberIds</code> parameters can't be used at the same time.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.describe_phone_numbers_request.DescribePhoneNumbersRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.describe_phone_numbers_result.DescribePhoneNumbersResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_phone_numbers

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_phone_numbers.async_describe_phone_numbers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.describe_phone_numbers_request.DescribePhoneNumbersRequest = {}
        if phone_number_ids is not None:
            input_["phone_number_ids"] = phone_number_ids
        if filters is not None:
            input_["filters"] = filters
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if owner is not None:
            input_["owner"] = owner

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_pools(
        self,
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        pool_ids: Optional[
            "capo_pinpoint_sms_voice_v2.types.pool_id_list.PoolIdList"
        ] = None,
        filters: Optional[
            "capo_pinpoint_sms_voice_v2.types.pool_filter_list.PoolFilterList"
        ] = None,
        next_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_pinpoint_sms_voice_v2.types.max_results.MaxResults"
        ] = None,
        owner: Optional["capo_pinpoint_sms_voice_v2.types.owner.Owner"] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.describe_pools_result.DescribePoolsResult":
        """<p>Retrieves the specified pools or all pools associated with your Amazon Web Services account.</p> <p>If you specify pool IDs, the output includes information for only the specified pools. If you specify filters, the output includes information for only those pools that meet the filter criteria. If you don't specify pool IDs or filters, the output includes information for all pools.</p> <p>If you specify a pool ID that isn't valid, an error is returned.</p> <p>A pool is a collection of phone numbers and SenderIds. A pool can include one or more phone numbers and SenderIds that are associated with your Amazon Web Services account.</p>

        Args:
            pool_ids: <p>The unique identifier of pools to find. This is an array of strings that can be either the PoolId or PoolArn.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>
            filters: <p>An array of PoolFilter objects to filter the results.</p>
            next_token: <p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>
            max_results: <p>The maximum number of results to return per each request.</p>
            owner: <p>Use <code>SELF</code> to filter the list of Pools to ones your account owns or use <code>SHARED</code> to filter on Pools shared with your account. The <code>Owner</code> and <code>PoolIds</code> parameters can't be used at the same time.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.describe_pools_request.DescribePoolsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.describe_pools_result.DescribePoolsResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_pools

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_pools.async_describe_pools(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.describe_pools_request.DescribePoolsRequest = {}
        if pool_ids is not None:
            input_["pool_ids"] = pool_ids
        if filters is not None:
            input_["filters"] = filters
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if owner is not None:
            input_["owner"] = owner

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_protect_configurations(
        self,
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        protect_configuration_ids: Optional[
            "capo_pinpoint_sms_voice_v2.types.protect_configuration_id_list.ProtectConfigurationIdList"
        ] = None,
        filters: Optional[
            "capo_pinpoint_sms_voice_v2.types.protect_configuration_filter_list.ProtectConfigurationFilterList"
        ] = None,
        next_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_pinpoint_sms_voice_v2.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.describe_protect_configurations_result.DescribeProtectConfigurationsResult":
        """<p>Retrieves the protect configurations that match any of filters. If a filter isn’t provided then all protect configurations are returned.</p>

        Args:
            protect_configuration_ids: <p>An array of protect configuration identifiers to search for.</p>
            filters: <p>An array of ProtectConfigurationFilter objects to filter the results.</p>
            next_token: <p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>
            max_results: <p>The maximum number of results to return per each request.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.describe_protect_configurations_request.DescribeProtectConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.describe_protect_configurations_result.DescribeProtectConfigurationsResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_protect_configurations

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_protect_configurations.async_describe_protect_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.describe_protect_configurations_request.DescribeProtectConfigurationsRequest = {}
        if protect_configuration_ids is not None:
            input_["protect_configuration_ids"] = protect_configuration_ids
        if filters is not None:
            input_["filters"] = filters
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

    async def describe_rcs_agent_country_launch_status(
        self,
        rcs_agent_id: "capo_pinpoint_sms_voice_v2.types.rcs_agent_id_or_arn.RcsAgentIdOrArn",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        iso_country_codes: Optional[
            "capo_pinpoint_sms_voice_v2.types.iso_country_code_list.IsoCountryCodeList"
        ] = None,
        filters: Optional[
            "capo_pinpoint_sms_voice_v2.types.country_launch_status_filter_list.CountryLaunchStatusFilterList"
        ] = None,
        max_results: Optional[
            "capo_pinpoint_sms_voice_v2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.next_token.NextToken"
        ] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.describe_rcs_agent_country_launch_status_result.DescribeRcsAgentCountryLaunchStatusResult":
        """<p>Retrieves the per-country launch status of an RCS agent, including carrier-level details for each country.</p>

        Args:
            rcs_agent_id: <p>The unique identifier of the RCS agent. You can use either the RcsAgentId or RcsAgentArn.</p>
            iso_country_codes: <p>An array of two-character ISO country codes, in ISO 3166-1 alpha-2 format, to filter the results.</p>
            filters: <p>An array of CountryLaunchStatusFilter objects to filter the results.</p>
            max_results: <p>The maximum number of results to return per each request.</p>
            next_token: <p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.describe_rcs_agent_country_launch_status_request.DescribeRcsAgentCountryLaunchStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.describe_rcs_agent_country_launch_status_result.DescribeRcsAgentCountryLaunchStatusResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_rcs_agent_country_launch_status

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_rcs_agent_country_launch_status.async_describe_rcs_agent_country_launch_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.describe_rcs_agent_country_launch_status_request.DescribeRcsAgentCountryLaunchStatusRequest = {
            "rcs_agent_id": rcs_agent_id
        }
        if iso_country_codes is not None:
            input_["iso_country_codes"] = iso_country_codes
        if filters is not None:
            input_["filters"] = filters
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

    async def describe_rcs_agents(
        self,
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        rcs_agent_ids: Optional[
            "capo_pinpoint_sms_voice_v2.types.rcs_agent_id_list.RcsAgentIdList"
        ] = None,
        owner: Optional["capo_pinpoint_sms_voice_v2.types.owner.Owner"] = None,
        filters: Optional[
            "capo_pinpoint_sms_voice_v2.types.rcs_agent_filter_list.RcsAgentFilterList"
        ] = None,
        next_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_pinpoint_sms_voice_v2.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.describe_rcs_agents_result.DescribeRcsAgentsResult":
        """<p>Retrieves the specified RCS agents or all RCS agents associated with your Amazon Web Services account.</p> <p>If you specify RCS agent IDs, the output includes information for only the specified RCS agents. If you specify filters, the output includes information for only those RCS agents that meet the filter criteria. If you don't specify RCS agent IDs or filters, the output includes information for all RCS agents.</p>

        Args:
            rcs_agent_ids: <p>An array of unique identifiers for the RCS agents. This is an array of strings that can be either the RcsAgentId or RcsAgentArn.</p>
            owner: <p>Use <code>SELF</code> to filter the list of RCS agents to ones your account owns or use <code>SHARED</code> to filter on RCS agents shared with your account. The <code>Owner</code> and <code>RcsAgentIds</code> parameters can't be used at the same time.</p>
            filters: <p>An array of RcsAgentFilter objects to filter the results.</p>
            next_token: <p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>
            max_results: <p>The maximum number of results to return per each request.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.describe_rcs_agents_request.DescribeRcsAgentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.describe_rcs_agents_result.DescribeRcsAgentsResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_rcs_agents

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_rcs_agents.async_describe_rcs_agents(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.describe_rcs_agents_request.DescribeRcsAgentsRequest = {}
        if rcs_agent_ids is not None:
            input_["rcs_agent_ids"] = rcs_agent_ids
        if owner is not None:
            input_["owner"] = owner
        if filters is not None:
            input_["filters"] = filters
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

    async def describe_registration_attachments(
        self,
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        registration_attachment_ids: Optional[
            "capo_pinpoint_sms_voice_v2.types.registration_attachment_id_list.RegistrationAttachmentIdList"
        ] = None,
        filters: Optional[
            "capo_pinpoint_sms_voice_v2.types.registration_attachment_filter_list.RegistrationAttachmentFilterList"
        ] = None,
        next_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_pinpoint_sms_voice_v2.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.describe_registration_attachments_result.DescribeRegistrationAttachmentsResult":
        """<p>Retrieves the specified registration attachments or all registration attachments associated with your Amazon Web Services account.</p>

        Args:
            registration_attachment_ids: <p>The unique identifier of registration attachments to find. This is an array of <b>RegistrationAttachmentId</b>.</p>
            filters: <p>An array of RegistrationAttachmentFilter objects to filter the results.</p>
            next_token: <p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>
            max_results: <p>The maximum number of results to return per each request.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.describe_registration_attachments_request.DescribeRegistrationAttachmentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.describe_registration_attachments_result.DescribeRegistrationAttachmentsResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_registration_attachments

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_registration_attachments.async_describe_registration_attachments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.describe_registration_attachments_request.DescribeRegistrationAttachmentsRequest = {}
        if registration_attachment_ids is not None:
            input_["registration_attachment_ids"] = registration_attachment_ids
        if filters is not None:
            input_["filters"] = filters
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

    async def describe_registration_field_definitions(
        self,
        registration_type: "capo_pinpoint_sms_voice_v2.types.registration_type.RegistrationType",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        section_path: Optional[
            "capo_pinpoint_sms_voice_v2.types.section_path.SectionPath"
        ] = None,
        field_paths: Optional[
            "capo_pinpoint_sms_voice_v2.types.field_path_list.FieldPathList"
        ] = None,
        next_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_pinpoint_sms_voice_v2.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.describe_registration_field_definitions_result.DescribeRegistrationFieldDefinitionsResult":
        """<p>Retrieves the specified registration type field definitions. You can use DescribeRegistrationFieldDefinitions to view the requirements for creating, filling out, and submitting each registration type.</p>

        Args:
            registration_type: <p>The type of registration form. The list of <b>RegistrationTypes</b> can be found using the <a>DescribeRegistrationTypeDefinitions</a> action.</p>
            section_path: <p>The path to the section of the registration.</p>
            field_paths: <p>An array of paths to the registration form field.</p>
            next_token: <p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>
            max_results: <p>The maximum number of results to return per each request.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.describe_registration_field_definitions_request.DescribeRegistrationFieldDefinitionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.describe_registration_field_definitions_result.DescribeRegistrationFieldDefinitionsResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_registration_field_definitions

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_registration_field_definitions.async_describe_registration_field_definitions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.describe_registration_field_definitions_request.DescribeRegistrationFieldDefinitionsRequest = {
            "registration_type": registration_type
        }
        if section_path is not None:
            input_["section_path"] = section_path
        if field_paths is not None:
            input_["field_paths"] = field_paths
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

    async def describe_registration_field_values(
        self,
        registration_id: "capo_pinpoint_sms_voice_v2.types.registration_id_or_arn.RegistrationIdOrArn",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        version_number: Optional[
            "capo_pinpoint_sms_voice_v2.types.registration_version_number.RegistrationVersionNumber"
        ] = None,
        section_path: Optional[
            "capo_pinpoint_sms_voice_v2.types.section_path.SectionPath"
        ] = None,
        field_paths: Optional[
            "capo_pinpoint_sms_voice_v2.types.field_path_list.FieldPathList"
        ] = None,
        next_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_pinpoint_sms_voice_v2.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.describe_registration_field_values_result.DescribeRegistrationFieldValuesResult":
        """<p>Retrieves the specified registration field values.</p>

        Args:
            registration_id: <p>The unique identifier for the registration.</p>
            version_number: <p>The version number of the registration.</p>
            section_path: <p>The path to the section of the registration.</p>
            field_paths: <p>An array of paths to the registration form field.</p>
            next_token: <p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>
            max_results: <p>The maximum number of results to return per each request.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.describe_registration_field_values_request.DescribeRegistrationFieldValuesRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.describe_registration_field_values_result.DescribeRegistrationFieldValuesResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_registration_field_values

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_registration_field_values.async_describe_registration_field_values(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.describe_registration_field_values_request.DescribeRegistrationFieldValuesRequest = {
            "registration_id": registration_id
        }
        if version_number is not None:
            input_["version_number"] = version_number
        if section_path is not None:
            input_["section_path"] = section_path
        if field_paths is not None:
            input_["field_paths"] = field_paths
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

    async def describe_registrations(
        self,
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        registration_ids: Optional[
            "capo_pinpoint_sms_voice_v2.types.registration_id_list.RegistrationIdList"
        ] = None,
        filters: Optional[
            "capo_pinpoint_sms_voice_v2.types.registration_filter_list.RegistrationFilterList"
        ] = None,
        next_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_pinpoint_sms_voice_v2.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.describe_registrations_result.DescribeRegistrationsResult":
        """<p>Retrieves the specified registrations.</p>

        Args:
            registration_ids: <p>An array of unique identifiers for each registration.</p>
            filters: <p>An array of RegistrationFilter objects to filter the results.</p>
            next_token: <p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>
            max_results: <p>The maximum number of results to return per each request.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.describe_registrations_request.DescribeRegistrationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.describe_registrations_result.DescribeRegistrationsResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_registrations

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_registrations.async_describe_registrations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.describe_registrations_request.DescribeRegistrationsRequest = {}
        if registration_ids is not None:
            input_["registration_ids"] = registration_ids
        if filters is not None:
            input_["filters"] = filters
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

    async def describe_registration_section_definitions(
        self,
        registration_type: "capo_pinpoint_sms_voice_v2.types.registration_type.RegistrationType",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        section_paths: Optional[
            "capo_pinpoint_sms_voice_v2.types.section_path_list.SectionPathList"
        ] = None,
        next_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_pinpoint_sms_voice_v2.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.describe_registration_section_definitions_result.DescribeRegistrationSectionDefinitionsResult":
        """<p>Retrieves the specified registration section definitions. You can use DescribeRegistrationSectionDefinitions to view the requirements for creating, filling out, and submitting each registration type.</p>

        Args:
            registration_type: <p>The type of registration form. The list of <b>RegistrationTypes</b> can be found using the <a>DescribeRegistrationTypeDefinitions</a> action.</p>
            section_paths: <p>An array of paths for the registration form section.</p>
            next_token: <p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>
            max_results: <p>The maximum number of results to return per each request.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.describe_registration_section_definitions_request.DescribeRegistrationSectionDefinitionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.describe_registration_section_definitions_result.DescribeRegistrationSectionDefinitionsResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_registration_section_definitions

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_registration_section_definitions.async_describe_registration_section_definitions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.describe_registration_section_definitions_request.DescribeRegistrationSectionDefinitionsRequest = {
            "registration_type": registration_type
        }
        if section_paths is not None:
            input_["section_paths"] = section_paths
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

    async def describe_registration_type_definitions(
        self,
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        registration_types: Optional[
            "capo_pinpoint_sms_voice_v2.types.registration_type_list.RegistrationTypeList"
        ] = None,
        filters: Optional[
            "capo_pinpoint_sms_voice_v2.types.registration_type_filter_list.RegistrationTypeFilterList"
        ] = None,
        next_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_pinpoint_sms_voice_v2.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.describe_registration_type_definitions_result.DescribeRegistrationTypeDefinitionsResult":
        """<p>Retrieves the specified registration type definitions. You can use DescribeRegistrationTypeDefinitions to view the requirements for creating, filling out, and submitting each registration type.</p>

        Args:
            registration_types: <p>The type of registration form. The list of <b>RegistrationTypes</b> can be found using the <a>DescribeRegistrationTypeDefinitions</a> action.</p>
            filters: <p>An array of RegistrationFilter objects to filter the results.</p>
            next_token: <p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>
            max_results: <p>The maximum number of results to return per each request.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.describe_registration_type_definitions_request.DescribeRegistrationTypeDefinitionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.describe_registration_type_definitions_result.DescribeRegistrationTypeDefinitionsResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_registration_type_definitions

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_registration_type_definitions.async_describe_registration_type_definitions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.describe_registration_type_definitions_request.DescribeRegistrationTypeDefinitionsRequest = {}
        if registration_types is not None:
            input_["registration_types"] = registration_types
        if filters is not None:
            input_["filters"] = filters
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

    async def describe_registration_versions(
        self,
        registration_id: "capo_pinpoint_sms_voice_v2.types.registration_id_or_arn.RegistrationIdOrArn",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        version_numbers: Optional[
            "capo_pinpoint_sms_voice_v2.types.registration_version_number_list.RegistrationVersionNumberList"
        ] = None,
        filters: Optional[
            "capo_pinpoint_sms_voice_v2.types.registration_version_filter_list.RegistrationVersionFilterList"
        ] = None,
        next_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_pinpoint_sms_voice_v2.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.describe_registration_versions_result.DescribeRegistrationVersionsResult":
        """<p>Retrieves the specified registration version.</p>

        Args:
            registration_id: <p>The unique identifier for the registration.</p>
            version_numbers: <p>An array of registration version numbers.</p>
            filters: <p>An array of RegistrationVersionFilter objects to filter the results.</p>
            next_token: <p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>
            max_results: <p>The maximum number of results to return per each request.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.describe_registration_versions_request.DescribeRegistrationVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.describe_registration_versions_result.DescribeRegistrationVersionsResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_registration_versions

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_registration_versions.async_describe_registration_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.describe_registration_versions_request.DescribeRegistrationVersionsRequest = {
            "registration_id": registration_id
        }
        if version_numbers is not None:
            input_["version_numbers"] = version_numbers
        if filters is not None:
            input_["filters"] = filters
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

    async def describe_sender_ids(
        self,
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        sender_ids: Optional[
            "capo_pinpoint_sms_voice_v2.types.sender_id_list.SenderIdList"
        ] = None,
        filters: Optional[
            "capo_pinpoint_sms_voice_v2.types.sender_id_filter_list.SenderIdFilterList"
        ] = None,
        next_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_pinpoint_sms_voice_v2.types.max_results.MaxResults"
        ] = None,
        owner: Optional["capo_pinpoint_sms_voice_v2.types.owner.Owner"] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.describe_sender_ids_result.DescribeSenderIdsResult":
        """<p>Describes the specified SenderIds or all SenderIds associated with your Amazon Web Services account.</p> <p>If you specify SenderIds, the output includes information for only the specified SenderIds. If you specify filters, the output includes information for only those SenderIds that meet the filter criteria. If you don't specify SenderIds or filters, the output includes information for all SenderIds.</p> <p>f you specify a sender ID that isn't valid, an error is returned.</p>

        Args:
            sender_ids: <p>An array of SenderIdAndCountry objects to search for.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>
            filters: <p>An array of SenderIdFilter objects to filter the results.</p>
            next_token: <p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>
            max_results: <p>The maximum number of results to return per each request.</p>
            owner: <p>Use <code>SELF</code> to filter the list of Sender Ids to ones your account owns or use <code>SHARED</code> to filter on Sender Ids shared with your account. The <code>Owner</code> and <code>SenderIds</code> parameters can't be used at the same time. </p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.describe_sender_ids_request.DescribeSenderIdsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.describe_sender_ids_result.DescribeSenderIdsResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_sender_ids

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_sender_ids.async_describe_sender_ids(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.describe_sender_ids_request.DescribeSenderIdsRequest = {}
        if sender_ids is not None:
            input_["sender_ids"] = sender_ids
        if filters is not None:
            input_["filters"] = filters
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if owner is not None:
            input_["owner"] = owner

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_spend_limits(
        self,
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        next_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_pinpoint_sms_voice_v2.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.describe_spend_limits_result.DescribeSpendLimitsResult":
        """<p>Describes the current monthly spend limits for sending voice and text messages.</p> <p>When you establish an Amazon Web Services account, the account has initial monthly spend limit in a given Region. For more information on increasing your monthly spend limit, see <a href="https://docs.aws.amazon.com/sms-voice/latest/userguide/awssupport-spend-threshold.html"> Requesting increases to your monthly SMS, MMS, or Voice spending quota </a> in the <i>End User Messaging SMS User Guide</i>.</p>

        Args:
            next_token: <p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>
            max_results: <p>The maximum number of results to return per each request.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.describe_spend_limits_request.DescribeSpendLimitsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.describe_spend_limits_result.DescribeSpendLimitsResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_spend_limits

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_spend_limits.async_describe_spend_limits(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.describe_spend_limits_request.DescribeSpendLimitsRequest = {}
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

    async def describe_verified_destination_numbers(
        self,
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        verified_destination_number_ids: Optional[
            "capo_pinpoint_sms_voice_v2.types.verified_destination_number_id_list.VerifiedDestinationNumberIdList"
        ] = None,
        destination_phone_numbers: Optional[
            "capo_pinpoint_sms_voice_v2.types.destination_phone_number_list.DestinationPhoneNumberList"
        ] = None,
        filters: Optional[
            "capo_pinpoint_sms_voice_v2.types.verified_destination_number_filter_list.VerifiedDestinationNumberFilterList"
        ] = None,
        next_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_pinpoint_sms_voice_v2.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.describe_verified_destination_numbers_result.DescribeVerifiedDestinationNumbersResult":
        """<p>Retrieves the specified verified destination numbers.</p>

        Args:
            verified_destination_number_ids: <p>An array of VerifiedDestinationNumberid to retrieve.</p>
            destination_phone_numbers: <p>An array of verified destination phone number, in E.164 format.</p>
            filters: <p>An array of VerifiedDestinationNumberFilter objects to filter the results.</p>
            next_token: <p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>
            max_results: <p>The maximum number of results to return per each request.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.describe_verified_destination_numbers_request.DescribeVerifiedDestinationNumbersRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.describe_verified_destination_numbers_result.DescribeVerifiedDestinationNumbersResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_verified_destination_numbers

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.describe_verified_destination_numbers.async_describe_verified_destination_numbers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.describe_verified_destination_numbers_request.DescribeVerifiedDestinationNumbersRequest = {}
        if verified_destination_number_ids is not None:
            input_["verified_destination_number_ids"] = verified_destination_number_ids
        if destination_phone_numbers is not None:
            input_["destination_phone_numbers"] = destination_phone_numbers
        if filters is not None:
            input_["filters"] = filters
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

    async def disassociate_origination_identity(
        self,
        pool_id: "capo_pinpoint_sms_voice_v2.types.pool_id_or_arn.PoolIdOrArn",
        origination_identity: "capo_pinpoint_sms_voice_v2.types.phone_or_sender_id_or_arn.PhoneOrSenderIdOrArn",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        iso_country_code: Optional[
            "capo_pinpoint_sms_voice_v2.types.iso_country_code.IsoCountryCode"
        ] = None,
        client_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.disassociate_origination_identity_result.DisassociateOriginationIdentityResult":
        """<p>Removes the specified origination identity from an existing pool.</p> <p>If the origination identity isn't associated with the specified pool, an error is returned.</p>

        Args:
            pool_id: <p>The unique identifier for the pool to disassociate with the origination identity. This value can be either the PoolId or PoolArn.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>
            origination_identity: <p>The origination identity to use such as a PhoneNumberId, PhoneNumberArn, SenderId or SenderIdArn. You can use <a>DescribePhoneNumbers</a> find the values for PhoneNumberId and PhoneNumberArn, or use <a>DescribeSenderIds</a> to get the values for SenderId and SenderIdArn.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>
            iso_country_code: <p>The two-character code, in ISO 3166-1 alpha-2 format, for the country or region. This field is optional and is not required for origination identity types that are not country-specific, such as RCS agents.</p>
            client_token: <p>Unique, case-sensitive identifier you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.disassociate_origination_identity_request.DisassociateOriginationIdentityRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.disassociate_origination_identity_result.DisassociateOriginationIdentityResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.disassociate_origination_identity

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.disassociate_origination_identity.async_disassociate_origination_identity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.disassociate_origination_identity_request.DisassociateOriginationIdentityRequest = {
            "pool_id": pool_id,
            "origination_identity": origination_identity,
        }
        if iso_country_code is not None:
            input_["iso_country_code"] = iso_country_code
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

    async def disassociate_protect_configuration(
        self,
        protect_configuration_id: "capo_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn.ProtectConfigurationIdOrArn",
        configuration_set_name: "capo_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn.ConfigurationSetNameOrArn",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.disassociate_protect_configuration_result.DisassociateProtectConfigurationResult":
        """<p>Disassociate a protect configuration from a configuration set.</p>

        Args:
            protect_configuration_id: <p>The unique identifier for the protect configuration.</p>
            configuration_set_name: <p>The name of the ConfigurationSet.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.disassociate_protect_configuration_request.DisassociateProtectConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.disassociate_protect_configuration_result.DisassociateProtectConfigurationResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.disassociate_protect_configuration

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.disassociate_protect_configuration.async_disassociate_protect_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.disassociate_protect_configuration_request.DisassociateProtectConfigurationRequest = {
            "protect_configuration_id": protect_configuration_id,
            "configuration_set_name": configuration_set_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def discard_registration_version(
        self,
        registration_id: "capo_pinpoint_sms_voice_v2.types.registration_id_or_arn.RegistrationIdOrArn",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.discard_registration_version_result.DiscardRegistrationVersionResult":
        """<p>Discard the current version of the registration.</p>

        Args:
            registration_id: <p>The unique identifier for the registration.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.discard_registration_version_request.DiscardRegistrationVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.discard_registration_version_result.DiscardRegistrationVersionResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.discard_registration_version

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.discard_registration_version.async_discard_registration_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.discard_registration_version_request.DiscardRegistrationVersionRequest = {
            "registration_id": registration_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_protect_configuration_country_rule_set(
        self,
        protect_configuration_id: "capo_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn.ProtectConfigurationIdOrArn",
        number_capability: "capo_pinpoint_sms_voice_v2.types.number_capability.NumberCapability",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.get_protect_configuration_country_rule_set_result.GetProtectConfigurationCountryRuleSetResult":
        """<p>Retrieve the CountryRuleSet for the specified NumberCapability from a protect configuration.</p>

        Args:
            protect_configuration_id: <p>The unique identifier for the protect configuration.</p>
            number_capability: <p>The capability type to return the CountryRuleSet for. Valid values are <code>SMS</code>, <code>VOICE</code>, or <code>MMS</code>.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.get_protect_configuration_country_rule_set_request.GetProtectConfigurationCountryRuleSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.get_protect_configuration_country_rule_set_result.GetProtectConfigurationCountryRuleSetResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.get_protect_configuration_country_rule_set

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.get_protect_configuration_country_rule_set.async_get_protect_configuration_country_rule_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.get_protect_configuration_country_rule_set_request.GetProtectConfigurationCountryRuleSetRequest = {
            "protect_configuration_id": protect_configuration_id,
            "number_capability": number_capability,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_resource_policy(
        self,
        resource_arn: "capo_pinpoint_sms_voice_v2.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.get_resource_policy_result.GetResourcePolicyResult":
        """<p>Retrieves the JSON text of the resource-based policy document attached to the End User Messaging SMS resource. A shared resource can be a Pool, Opt-out list, Sender Id, or Phone number.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the End User Messaging SMS resource attached to the resource-based policy.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.get_resource_policy_request.GetResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.get_resource_policy_result.GetResourcePolicyResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.get_resource_policy

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.get_resource_policy.async_get_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.get_resource_policy_request.GetResourcePolicyRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_available_phone_numbers(
        self,
        iso_country_code: "capo_pinpoint_sms_voice_v2.types.iso_country_code.IsoCountryCode",
        number_capabilities: "capo_pinpoint_sms_voice_v2.types.number_capability_list.NumberCapabilityList",
        number_type: "capo_pinpoint_sms_voice_v2.types.searchable_number_type.SearchableNumberType",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        registration_id: Optional[
            "capo_pinpoint_sms_voice_v2.types.registration_id_or_arn.RegistrationIdOrArn"
        ] = None,
        number_preference: Optional[
            "capo_pinpoint_sms_voice_v2.types.number_preference_list.NumberPreferenceList"
        ] = None,
        next_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_pinpoint_sms_voice_v2.types.list_available_phone_numbers_max_results.ListAvailablePhoneNumbersMaxResults"
        ] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.list_available_phone_numbers_result.ListAvailablePhoneNumbersResult":
        """<p>Retrieves a list of phone numbers that are available to request, based on the country, capabilities, and number type that you specify. You can optionally provide a number preference to return only numbers that match a specific digit pattern.</p> <p>If no numbers match your search, this operation returns an empty list rather than an error. This operation currently supports only <code>TEN_DLC</code> number types in the <code>US</code>.</p>

        Args:
            iso_country_code: <p>The two-character code, in ISO 3166-1 alpha-2 format, for the country or region in which to search for available phone numbers. This operation currently supports only <code>US</code>.</p>
            number_capabilities: <p>The capabilities to filter by, such as SMS. Only phone numbers that support all of the specified capabilities are returned.</p>
            number_type: <p>The type of phone number to search for.</p>
            registration_id: <p>The registration associated with the request. A registration is required for regulated number types. You can specify either:</p> <ul> <li> <p>The unique identifier of the registration.</p> </li> <li> <p>The Amazon Resource Name (ARN) of the registration.</p> </li> </ul>
            number_preference: <p>An optional selection preference used to return only phone numbers that match a specific digit pattern, such as numbers that start with, end with, or contain a particular sequence. You can specify at most one preference. Number preferences apply only to <code>TEN_DLC</code> numbers in the <code>US</code>.</p>
            next_token: <p>The token returned from a previous request to retrieve the next page of results.</p>
            max_results: <p>The maximum number of results to return per page. If you don't specify a value, the default is 10.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ListAvailablePhoneNumbers
            Search for available TEN_DLC phone numbers in the US that start with a specific area code.

            >>> await client.list_available_phone_numbers(iso_country_code='US', number_capabilities=['SMS'], number_type='TEN_DLC', registration_id='reg-1234567890abcdef0', number_preference=[{'PreferenceType': ['StartsWith'], 'Filter': ['+1206']}], max_results=10)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.list_available_phone_numbers_request.ListAvailablePhoneNumbersRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.list_available_phone_numbers_result.ListAvailablePhoneNumbersResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.list_available_phone_numbers

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.list_available_phone_numbers.async_list_available_phone_numbers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.list_available_phone_numbers_request.ListAvailablePhoneNumbersRequest = {
            "iso_country_code": iso_country_code,
            "number_capabilities": number_capabilities,
            "number_type": number_type,
        }
        if registration_id is not None:
            input_["registration_id"] = registration_id
        if number_preference is not None:
            input_["number_preference"] = number_preference
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

    async def list_notify_countries(
        self,
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        channels: Optional[
            "capo_pinpoint_sms_voice_v2.types.notify_enabled_channels_list.NotifyEnabledChannelsList"
        ] = None,
        use_cases: Optional[
            "capo_pinpoint_sms_voice_v2.types.notify_use_case_list.NotifyUseCaseList"
        ] = None,
        tier: Optional[
            "capo_pinpoint_sms_voice_v2.types.notify_configuration_tier.NotifyConfigurationTier"
        ] = None,
        next_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_pinpoint_sms_voice_v2.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.list_notify_countries_result.ListNotifyCountriesResult":
        """<p>Lists countries that support notify messaging. You can optionally filter by channel, use case, or tier.</p>

        Args:
            channels: <p>An array of channels to filter the results by.</p>
            use_cases: <p>An array of use cases to filter the results by.</p>
            tier: <p>The tier to filter the results by.</p>
            next_token: <p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>
            max_results: <p>The maximum number of results to return per each request.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ListNotifyCountries
            List countries that support notify messaging over SMS.

            >>> await client.list_notify_countries(channels=['SMS'], max_results=10)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.list_notify_countries_request.ListNotifyCountriesRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.list_notify_countries_result.ListNotifyCountriesResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.list_notify_countries

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.list_notify_countries.async_list_notify_countries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.list_notify_countries_request.ListNotifyCountriesRequest = {}
        if channels is not None:
            input_["channels"] = channels
        if use_cases is not None:
            input_["use_cases"] = use_cases
        if tier is not None:
            input_["tier"] = tier
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

    async def list_pool_origination_identities(
        self,
        pool_id: "capo_pinpoint_sms_voice_v2.types.pool_id_or_arn.PoolIdOrArn",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        filters: Optional[
            "capo_pinpoint_sms_voice_v2.types.pool_origination_identities_filter_list.PoolOriginationIdentitiesFilterList"
        ] = None,
        next_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_pinpoint_sms_voice_v2.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.list_pool_origination_identities_result.ListPoolOriginationIdentitiesResult":
        """<p>Lists all associated origination identities in your pool.</p> <p>If you specify filters, the output includes information for only those origination identities that meet the filter criteria.</p>

        Args:
            pool_id: <p>The unique identifier for the pool. This value can be either the PoolId or PoolArn.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>
            filters: <p>An array of PoolOriginationIdentitiesFilter objects to filter the results..</p>
            next_token: <p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>
            max_results: <p>The maximum number of results to return per each request.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.list_pool_origination_identities_request.ListPoolOriginationIdentitiesRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.list_pool_origination_identities_result.ListPoolOriginationIdentitiesResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.list_pool_origination_identities

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.list_pool_origination_identities.async_list_pool_origination_identities(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.list_pool_origination_identities_request.ListPoolOriginationIdentitiesRequest = {
            "pool_id": pool_id
        }
        if filters is not None:
            input_["filters"] = filters
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

    async def list_protect_configuration_rule_set_number_overrides(
        self,
        protect_configuration_id: "capo_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn.ProtectConfigurationIdOrArn",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        filters: Optional[
            "capo_pinpoint_sms_voice_v2.types.list_protect_configuration_rule_set_number_override_filter.ListProtectConfigurationRuleSetNumberOverrideFilter"
        ] = None,
        next_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_pinpoint_sms_voice_v2.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.list_protect_configuration_rule_set_number_overrides_result.ListProtectConfigurationRuleSetNumberOverridesResult":
        """<p>Retrieve all of the protect configuration rule set number overrides that match the filters.</p>

        Args:
            protect_configuration_id: <p>The unique identifier for the protect configuration.</p>
            filters: <p>An array of ProtectConfigurationRuleSetNumberOverrideFilterItem objects to filter the results.</p>
            next_token: <p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>
            max_results: <p>The maximum number of results to return per each request.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.list_protect_configuration_rule_set_number_overrides_request.ListProtectConfigurationRuleSetNumberOverridesRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.list_protect_configuration_rule_set_number_overrides_result.ListProtectConfigurationRuleSetNumberOverridesResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.list_protect_configuration_rule_set_number_overrides

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.list_protect_configuration_rule_set_number_overrides.async_list_protect_configuration_rule_set_number_overrides(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.list_protect_configuration_rule_set_number_overrides_request.ListProtectConfigurationRuleSetNumberOverridesRequest = {
            "protect_configuration_id": protect_configuration_id
        }
        if filters is not None:
            input_["filters"] = filters
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

    async def list_registration_associations(
        self,
        registration_id: "capo_pinpoint_sms_voice_v2.types.registration_id_or_arn.RegistrationIdOrArn",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        filters: Optional[
            "capo_pinpoint_sms_voice_v2.types.registration_association_filter_list.RegistrationAssociationFilterList"
        ] = None,
        next_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_pinpoint_sms_voice_v2.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.list_registration_associations_result.ListRegistrationAssociationsResult":
        """<p>Retrieve all of the origination identities that are associated with a registration.</p>

        Args:
            registration_id: <p>The unique identifier for the registration.</p>
            filters: <p>An array of RegistrationAssociationFilter to apply to the results that are returned.</p>
            next_token: <p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>
            max_results: <p>The maximum number of results to return per each request.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.list_registration_associations_request.ListRegistrationAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.list_registration_associations_result.ListRegistrationAssociationsResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.list_registration_associations

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.list_registration_associations.async_list_registration_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.list_registration_associations_request.ListRegistrationAssociationsRequest = {
            "registration_id": registration_id
        }
        if filters is not None:
            input_["filters"] = filters
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

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_pinpoint_sms_voice_v2.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.list_tags_for_resource_result.ListTagsForResourceResult":
        """<p>List all tags associated with a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to query for.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.list_tags_for_resource_result.ListTagsForResourceResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_keyword(
        self,
        origination_identity: "capo_pinpoint_sms_voice_v2.types.phone_or_pool_id_or_arn.PhoneOrPoolIdOrArn",
        keyword: "capo_pinpoint_sms_voice_v2.types.keyword.Keyword",
        keyword_message: "capo_pinpoint_sms_voice_v2.types.keyword_message.KeywordMessage",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        keyword_action: Optional[
            "capo_pinpoint_sms_voice_v2.types.keyword_action.KeywordAction"
        ] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.put_keyword_result.PutKeywordResult":
        """<p>Creates or updates a keyword configuration on an origination phone number or pool.</p> <p> A keyword is a word that you can search for on a particular phone number or pool. It is also a specific word or phrase that an end user can send to your number to elicit a response, such as an informational message or a special offer. When your number receives a message that begins with a keyword, End User Messaging SMS responds with a customizable message.</p> <p>If you specify a keyword that isn't valid, an error is returned.</p>

        Args:
            origination_identity: <p>The origination identity to use such as a PhoneNumberId, PhoneNumberArn, SenderId or SenderIdArn. You can use <a>DescribePhoneNumbers</a> get the values for PhoneNumberId and PhoneNumberArn while <a>DescribeSenderIds</a> can be used to get the values for SenderId and SenderIdArn.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>
            keyword: <p>The new keyword to add.</p>
            keyword_message: <p>The message associated with the keyword.</p>
            keyword_action: <p>The action to perform for the new keyword when it is received.</p> <ul> <li> <p>AUTOMATIC_RESPONSE: A message is sent to the recipient.</p> </li> <li> <p>OPT_OUT: Keeps the recipient from receiving future messages.</p> </li> <li> <p>OPT_IN: The recipient wants to receive future messages.</p> </li> </ul>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.put_keyword_request.PutKeywordRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.put_keyword_result.PutKeywordResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.put_keyword

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.put_keyword.async_put_keyword(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.put_keyword_request.PutKeywordRequest = {
            "origination_identity": origination_identity,
            "keyword": keyword,
            "keyword_message": keyword_message,
        }
        if keyword_action is not None:
            input_["keyword_action"] = keyword_action

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_message_feedback(
        self,
        message_id: "capo_pinpoint_sms_voice_v2.types.message_id.MessageId",
        message_feedback_status: "capo_pinpoint_sms_voice_v2.types.message_feedback_status.MessageFeedbackStatus",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.put_message_feedback_result.PutMessageFeedbackResult":
        """<p>Set the MessageFeedbackStatus as <code>RECEIVED</code> or <code>FAILED</code> for the passed in MessageId. </p> <p>If you use message feedback then you must update message feedback record. When you receive a signal that a user has received the message you must use <code>PutMessageFeedback</code> to set the message feedback record as <code>RECEIVED</code>; Otherwise, an hour after the message feedback record is set to <code>FAILED</code>.</p>

        Args:
            message_id: <p>The unique identifier for the message.</p>
            message_feedback_status: <p>Set the message feedback to be either <code>RECEIVED</code> or <code>FAILED</code>.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.put_message_feedback_request.PutMessageFeedbackRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.put_message_feedback_result.PutMessageFeedbackResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.put_message_feedback

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.put_message_feedback.async_put_message_feedback(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.put_message_feedback_request.PutMessageFeedbackRequest = {
            "message_id": message_id,
            "message_feedback_status": message_feedback_status,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_opted_out_number(
        self,
        opt_out_list_name: "capo_pinpoint_sms_voice_v2.types.opt_out_list_name_or_arn.OptOutListNameOrArn",
        opted_out_number: "capo_pinpoint_sms_voice_v2.types.phone_number.PhoneNumber",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.put_opted_out_number_result.PutOptedOutNumberResult":
        """<p>Creates an opted out destination phone number in the opt-out list.</p> <p>If the destination phone number isn't valid or if the specified opt-out list doesn't exist, an error is returned.</p>

        Args:
            opt_out_list_name: <p>The OptOutListName or OptOutListArn to add the phone number to.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>
            opted_out_number: <p>The phone number to add to the OptOutList in E.164 format.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.put_opted_out_number_request.PutOptedOutNumberRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.put_opted_out_number_result.PutOptedOutNumberResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.put_opted_out_number

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.put_opted_out_number.async_put_opted_out_number(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.put_opted_out_number_request.PutOptedOutNumberRequest = {
            "opt_out_list_name": opt_out_list_name,
            "opted_out_number": opted_out_number,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_protect_configuration_rule_set_number_override(
        self,
        protect_configuration_id: "capo_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn.ProtectConfigurationIdOrArn",
        destination_phone_number: "capo_pinpoint_sms_voice_v2.types.phone_number.PhoneNumber",
        action: "capo_pinpoint_sms_voice_v2.types.protect_configuration_rule_override_action.ProtectConfigurationRuleOverrideAction",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        client_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.client_token.ClientToken"
        ] = None,
        expiration_timestamp: Optional[datetime.datetime] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.put_protect_configuration_rule_set_number_override_result.PutProtectConfigurationRuleSetNumberOverrideResult":
        """<p>Create or update a phone number rule override and associate it with a protect configuration.</p>

        Args:
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>
            protect_configuration_id: <p>The unique identifier for the protect configuration.</p>
            destination_phone_number: <p>The destination phone number in E.164 format.</p>
            action: <p>The action for the rule to either block or allow messages to the destination phone number.</p>
            expiration_timestamp: <p>The time the rule will expire at. If <code>ExpirationTimestamp</code> is not set then the rule does not expire.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.put_protect_configuration_rule_set_number_override_request.PutProtectConfigurationRuleSetNumberOverrideRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.put_protect_configuration_rule_set_number_override_result.PutProtectConfigurationRuleSetNumberOverrideResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.put_protect_configuration_rule_set_number_override

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.put_protect_configuration_rule_set_number_override.async_put_protect_configuration_rule_set_number_override(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.put_protect_configuration_rule_set_number_override_request.PutProtectConfigurationRuleSetNumberOverrideRequest = {
            "protect_configuration_id": protect_configuration_id,
            "destination_phone_number": destination_phone_number,
            "action": action,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if expiration_timestamp is not None:
            input_["expiration_timestamp"] = expiration_timestamp

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_registration_field_value(
        self,
        registration_id: "capo_pinpoint_sms_voice_v2.types.registration_id_or_arn.RegistrationIdOrArn",
        field_path: "capo_pinpoint_sms_voice_v2.types.field_path.FieldPath",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        select_choices: Optional[
            "capo_pinpoint_sms_voice_v2.types.select_choice_list.SelectChoiceList"
        ] = None,
        text_value: Optional[
            "capo_pinpoint_sms_voice_v2.types.text_value.TextValue"
        ] = None,
        registration_attachment_id: Optional[
            "capo_pinpoint_sms_voice_v2.types.registration_attachment_id_or_arn.RegistrationAttachmentIdOrArn"
        ] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.put_registration_field_value_result.PutRegistrationFieldValueResult":
        """<p>Creates or updates a field value for a registration.</p>

        Args:
            registration_id: <p>The unique identifier for the registration.</p>
            field_path: <p>The path to the registration form field. You can use <a>DescribeRegistrationFieldDefinitions</a> for a list of <b>FieldPaths</b>.</p>
            select_choices: <p>An array of values for the form field.</p>
            text_value: <p>The text data for a free form field.</p>
            registration_attachment_id: <p>The unique identifier for the registration attachment.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.put_registration_field_value_request.PutRegistrationFieldValueRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.put_registration_field_value_result.PutRegistrationFieldValueResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.put_registration_field_value

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.put_registration_field_value.async_put_registration_field_value(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.put_registration_field_value_request.PutRegistrationFieldValueRequest = {
            "registration_id": registration_id,
            "field_path": field_path,
        }
        if select_choices is not None:
            input_["select_choices"] = select_choices
        if text_value is not None:
            input_["text_value"] = text_value
        if registration_attachment_id is not None:
            input_["registration_attachment_id"] = registration_attachment_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_resource_policy(
        self,
        resource_arn: "capo_pinpoint_sms_voice_v2.types.amazon_resource_name.AmazonResourceName",
        policy: "capo_pinpoint_sms_voice_v2.types.resource_policy.ResourcePolicy",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.put_resource_policy_result.PutResourcePolicyResult":
        """<p>Attaches a resource-based policy to a End User Messaging SMS resource(phone number, sender Id, phone poll, or opt-out list) that is used for sharing the resource. A shared resource can be a Pool, Opt-out list, Sender Id, or Phone number. For more information about resource-based policies, see <a href="https://docs.aws.amazon.com/sms-voice/latest/userguide/shared-resources.html">Working with shared resources</a> in the <i>End User Messaging SMS User Guide</i>. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the End User Messaging SMS resource to attach the resource-based policy to.</p>
            policy: <p>The JSON formatted resource-based policy to attach.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.put_resource_policy_request.PutResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.put_resource_policy_result.PutResourcePolicyResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.put_resource_policy

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.put_resource_policy.async_put_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.put_resource_policy_request.PutResourcePolicyRequest = {
            "resource_arn": resource_arn,
            "policy": policy,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def release_phone_number(
        self,
        phone_number_id: "capo_pinpoint_sms_voice_v2.types.phone_number_id_or_arn.PhoneNumberIdOrArn",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.release_phone_number_result.ReleasePhoneNumberResult":
        """<p>Releases an existing origination phone number in your account. Once released, a phone number is no longer available for sending messages.</p> <p>If the origination phone number has deletion protection enabled or is associated with a pool, an error is returned.</p>

        Args:
            phone_number_id: <p>The PhoneNumberId or PhoneNumberArn of the phone number to release. You can use <a>DescribePhoneNumbers</a> to get the values for PhoneNumberId and PhoneNumberArn.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.release_phone_number_request.ReleasePhoneNumberRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.release_phone_number_result.ReleasePhoneNumberResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.release_phone_number

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.release_phone_number.async_release_phone_number(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.release_phone_number_request.ReleasePhoneNumberRequest = {
            "phone_number_id": phone_number_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def release_sender_id(
        self,
        sender_id: "capo_pinpoint_sms_voice_v2.types.sender_id_or_arn.SenderIdOrArn",
        iso_country_code: "capo_pinpoint_sms_voice_v2.types.iso_country_code.IsoCountryCode",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.release_sender_id_result.ReleaseSenderIdResult":
        """<p>Releases an existing sender ID in your account.</p>

        Args:
            sender_id: <p>The sender ID to release.</p>
            iso_country_code: <p>The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.release_sender_id_request.ReleaseSenderIdRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.release_sender_id_result.ReleaseSenderIdResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.release_sender_id

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.release_sender_id.async_release_sender_id(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.release_sender_id_request.ReleaseSenderIdRequest = {
            "sender_id": sender_id,
            "iso_country_code": iso_country_code,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def request_phone_number(
        self,
        iso_country_code: "capo_pinpoint_sms_voice_v2.types.iso_country_code.IsoCountryCode",
        message_type: "capo_pinpoint_sms_voice_v2.types.message_type.MessageType",
        number_capabilities: "capo_pinpoint_sms_voice_v2.types.number_capability_list.NumberCapabilityList",
        number_type: "capo_pinpoint_sms_voice_v2.types.requestable_number_type.RequestableNumberType",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        opt_out_list_name: Optional[
            "capo_pinpoint_sms_voice_v2.types.opt_out_list_name_or_arn.OptOutListNameOrArn"
        ] = None,
        pool_id: Optional[
            "capo_pinpoint_sms_voice_v2.types.pool_id_or_arn.PoolIdOrArn"
        ] = None,
        registration_id: Optional[
            "capo_pinpoint_sms_voice_v2.types.registration_id_or_arn.RegistrationIdOrArn"
        ] = None,
        number_preference: Optional[
            "capo_pinpoint_sms_voice_v2.types.number_preference_list.NumberPreferenceList"
        ] = None,
        international_sending_enabled: Optional[bool] = None,
        deletion_protection_enabled: Optional[bool] = None,
        tags: Optional["capo_pinpoint_sms_voice_v2.types.tag_list.TagList"] = None,
        client_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.request_phone_number_result.RequestPhoneNumberResult":
        """<p>Request an origination phone number for use in your account. For more information on phone number request see <a href="https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-request.html">Request a phone number</a> in the <i>End User Messaging SMS User Guide</i>.</p>

        Args:
            iso_country_code: <p>The two-character code, in ISO 3166-1 alpha-2 format, for the country or region. </p>
            message_type: <p>The type of message. Valid values are <code>TRANSACTIONAL</code> for messages that are critical or time-sensitive and <code>PROMOTIONAL</code> for messages that aren't critical or time-sensitive.</p>
            number_capabilities: <p>Indicates if the phone number will be used for text messages, voice messages, or both. </p>
            number_type: <p>The type of phone number to request.</p> <p>When you request a <code>SIMULATOR</code> phone number, you must set <b>MessageType</b> as <code>TRANSACTIONAL</code>. </p>
            opt_out_list_name: <p>The name of the OptOutList to associate with the phone number. You can use the OptOutListName or OptOutListArn.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>
            pool_id: <p>The pool to associated with the phone number. You can use the PoolId or PoolArn. </p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>
            registration_id: <p>Use this field to attach your phone number for an external registration process.</p>
            number_preference: <p>An optional selection preference used to request a specific phone number, such as a number that starts with, ends with, or contains a particular digit pattern. You can specify at most one preference. Number preferences apply only to <code>TEN_DLC</code> requests in the <code>US</code>.</p>
            international_sending_enabled: <p>By default this is set to false. When set to true the international sending of phone number is Enabled. </p>
            deletion_protection_enabled: <p>By default this is set to false. When set to true the phone number can't be deleted.</p>
            tags: <p>An array of tags (key and value pairs) to associate with the requested phone number. </p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.request_phone_number_request.RequestPhoneNumberRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.request_phone_number_result.RequestPhoneNumberResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.request_phone_number

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.request_phone_number.async_request_phone_number(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.request_phone_number_request.RequestPhoneNumberRequest = {
            "iso_country_code": iso_country_code,
            "message_type": message_type,
            "number_capabilities": number_capabilities,
            "number_type": number_type,
        }
        if opt_out_list_name is not None:
            input_["opt_out_list_name"] = opt_out_list_name
        if pool_id is not None:
            input_["pool_id"] = pool_id
        if registration_id is not None:
            input_["registration_id"] = registration_id
        if number_preference is not None:
            input_["number_preference"] = number_preference
        if international_sending_enabled is not None:
            input_["international_sending_enabled"] = international_sending_enabled
        if deletion_protection_enabled is not None:
            input_["deletion_protection_enabled"] = deletion_protection_enabled
        if tags is not None:
            input_["tags"] = tags
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

    async def request_sender_id(
        self,
        sender_id: "capo_pinpoint_sms_voice_v2.types.sender_id.SenderId",
        iso_country_code: "capo_pinpoint_sms_voice_v2.types.iso_country_code.IsoCountryCode",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        message_types: Optional[
            "capo_pinpoint_sms_voice_v2.types.message_type_list.MessageTypeList"
        ] = None,
        deletion_protection_enabled: Optional[bool] = None,
        tags: Optional["capo_pinpoint_sms_voice_v2.types.tag_list.TagList"] = None,
        client_token: Optional[
            "capo_pinpoint_sms_voice_v2.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.request_sender_id_result.RequestSenderIdResult":
        """<p>Request a new sender ID that doesn't require registration. </p>

        Args:
            sender_id: <p>The sender ID string to request. The sender ID can be 1-11 alphanumeric characters including letters (A-Z, a-z), numbers (0-9), or hyphens (-). The sender ID must contain at least one letter and cannot start or end with a hyphen.</p>
            iso_country_code: <p>The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.</p>
            message_types: <p>The type of message. Valid values are TRANSACTIONAL for messages that are critical or time-sensitive and PROMOTIONAL for messages that aren't critical or time-sensitive.</p>
            deletion_protection_enabled: <p>By default this is set to false. When set to true the sender ID can't be deleted.</p>
            tags: <p>An array of tags (key and value pairs) to associate with the sender ID.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.request_sender_id_request.RequestSenderIdRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.request_sender_id_result.RequestSenderIdResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.request_sender_id

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.request_sender_id.async_request_sender_id(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.request_sender_id_request.RequestSenderIdRequest = {
            "sender_id": sender_id,
            "iso_country_code": iso_country_code,
        }
        if message_types is not None:
            input_["message_types"] = message_types
        if deletion_protection_enabled is not None:
            input_["deletion_protection_enabled"] = deletion_protection_enabled
        if tags is not None:
            input_["tags"] = tags
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

    async def send_destination_number_verification_code(
        self,
        verified_destination_number_id: "capo_pinpoint_sms_voice_v2.types.verified_destination_number_id_or_arn.VerifiedDestinationNumberIdOrArn",
        verification_channel: "capo_pinpoint_sms_voice_v2.types.verification_channel.VerificationChannel",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        language_code: Optional[
            "capo_pinpoint_sms_voice_v2.types.language_code.LanguageCode"
        ] = None,
        origination_identity: Optional[
            "capo_pinpoint_sms_voice_v2.types.verification_message_origination_identity.VerificationMessageOriginationIdentity"
        ] = None,
        configuration_set_name: Optional[
            "capo_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn.ConfigurationSetNameOrArn"
        ] = None,
        context: Optional[
            "capo_pinpoint_sms_voice_v2.types.context_map.ContextMap"
        ] = None,
        destination_country_parameters: Optional[
            "capo_pinpoint_sms_voice_v2.types.destination_country_parameters.DestinationCountryParameters"
        ] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.send_destination_number_verification_code_result.SendDestinationNumberVerificationCodeResult":
        """<p>Before you can send test messages to a verified destination phone number you need to opt-in the verified destination phone number. Creates a new text message with a verification code and send it to a verified destination phone number. Once you have the verification code use <a>VerifyDestinationNumber</a> to opt-in the verified destination phone number to receive messages.</p>

        Args:
            verified_destination_number_id: <p>The unique identifier for the verified destination phone number.</p>
            verification_channel: <p>Choose to send the verification code as an SMS or voice message.</p>
            language_code: <p>Choose the language to use for the message.</p>
            origination_identity: <p>The origination identity of the message. This can be either the PhoneNumber, PhoneNumberId, PhoneNumberArn, SenderId, SenderIdArn, PoolId, or PoolArn.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>
            configuration_set_name: <p>The name of the configuration set to use. This can be either the ConfigurationSetName or ConfigurationSetArn.</p>
            context: <p>You can specify custom data in this field. If you do, that data is logged to the event destination.</p>
            destination_country_parameters: <p>This field is used for any country-specific registration requirements. Currently, this setting is only used when you send messages to recipients in India using a sender ID. For more information see <a href="https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms-senderid-india.html">Special requirements for sending SMS messages to recipients in India</a>. </p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.send_destination_number_verification_code_request.SendDestinationNumberVerificationCodeRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.send_destination_number_verification_code_result.SendDestinationNumberVerificationCodeResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.send_destination_number_verification_code

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.send_destination_number_verification_code.async_send_destination_number_verification_code(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.send_destination_number_verification_code_request.SendDestinationNumberVerificationCodeRequest = {
            "verified_destination_number_id": verified_destination_number_id,
            "verification_channel": verification_channel,
        }
        if language_code is not None:
            input_["language_code"] = language_code
        if origination_identity is not None:
            input_["origination_identity"] = origination_identity
        if configuration_set_name is not None:
            input_["configuration_set_name"] = configuration_set_name
        if context is not None:
            input_["context"] = context
        if destination_country_parameters is not None:
            input_["destination_country_parameters"] = destination_country_parameters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def send_media_message(
        self,
        destination_phone_number: "capo_pinpoint_sms_voice_v2.types.phone_number.PhoneNumber",
        origination_identity: "capo_pinpoint_sms_voice_v2.types.media_message_origination_identity.MediaMessageOriginationIdentity",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        message_body: Optional[
            "capo_pinpoint_sms_voice_v2.types.text_message_body.TextMessageBody"
        ] = None,
        media_urls: Optional[
            "capo_pinpoint_sms_voice_v2.types.media_url_list.MediaUrlList"
        ] = None,
        configuration_set_name: Optional[
            "capo_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn.ConfigurationSetNameOrArn"
        ] = None,
        max_price: Optional[
            "capo_pinpoint_sms_voice_v2.types.max_price.MaxPrice"
        ] = None,
        time_to_live: Optional[
            "capo_pinpoint_sms_voice_v2.types.time_to_live.TimeToLive"
        ] = None,
        context: Optional[
            "capo_pinpoint_sms_voice_v2.types.context_map.ContextMap"
        ] = None,
        dry_run: Optional[bool] = None,
        protect_configuration_id: Optional[
            "capo_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn.ProtectConfigurationIdOrArn"
        ] = None,
        message_feedback_enabled: Optional[bool] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.send_media_message_result.SendMediaMessageResult":
        """<p>Creates a new multimedia message (MMS) and sends it to a recipient's phone number. </p>

        Args:
            destination_phone_number: <p>The destination phone number in E.164 format.</p>
            origination_identity: <p>The origination identity of the message. This can be either the PhoneNumber, PhoneNumberId, PhoneNumberArn, SenderId, SenderIdArn, PoolId, or PoolArn.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>
            message_body: <p>The text body of the message.</p>
            media_urls: <p>An array of URLs to each media file to send. </p> <p>The media files have to be stored in an S3 bucket. Supported media file formats are listed in <a href="https://docs.aws.amazon.com/sms-voice/latest/userguide/mms-limitations-character.html">MMS file types, size and character limits</a>. For more information on creating an S3 bucket and managing objects, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html">Creating a bucket</a>, <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html">Uploading objects</a> in the <i>Amazon S3 User Guide</i>, and <a href="https://docs.aws.amazon.com/sms-voice/latest/userguide/send-mms-message.html#send-mms-message-bucket">Setting up an Amazon S3 bucket for MMS files</a> in the <i>Amazon Web Services End User Messaging SMS User Guide</i>.</p>
            configuration_set_name: <p>The name of the configuration set to use. This can be either the ConfigurationSetName or ConfigurationSetArn.</p>
            max_price: <p>The maximum amount that you want to spend, in US dollars, per each MMS message.</p>
            time_to_live: <p>How long the media message is valid for. By default this is 72 hours.</p>
            context: <p>You can specify custom data in this field. If you do, that data is logged to the event destination.</p>
            dry_run: <p>When set to true, the message is checked and validated, but isn't sent to the end recipient.</p>
            protect_configuration_id: <p>The unique identifier of the protect configuration to use.</p>
            message_feedback_enabled: <p>Set to true to enable message feedback for the message. When a user receives the message you need to update the message status using <a>PutMessageFeedback</a>.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.send_media_message_request.SendMediaMessageRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.send_media_message_result.SendMediaMessageResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.send_media_message

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.send_media_message.async_send_media_message(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.send_media_message_request.SendMediaMessageRequest = {
            "destination_phone_number": destination_phone_number,
            "origination_identity": origination_identity,
        }
        if message_body is not None:
            input_["message_body"] = message_body
        if media_urls is not None:
            input_["media_urls"] = media_urls
        if configuration_set_name is not None:
            input_["configuration_set_name"] = configuration_set_name
        if max_price is not None:
            input_["max_price"] = max_price
        if time_to_live is not None:
            input_["time_to_live"] = time_to_live
        if context is not None:
            input_["context"] = context
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if protect_configuration_id is not None:
            input_["protect_configuration_id"] = protect_configuration_id
        if message_feedback_enabled is not None:
            input_["message_feedback_enabled"] = message_feedback_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def send_notify_text_message(
        self,
        notify_configuration_id: "capo_pinpoint_sms_voice_v2.types.notify_configuration_id_or_arn.NotifyConfigurationIdOrArn",
        destination_phone_number: "capo_pinpoint_sms_voice_v2.types.phone_number.PhoneNumber",
        template_variables: "capo_pinpoint_sms_voice_v2.types.template_variable_substitution_map.TemplateVariableSubstitutionMap",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        template_id: Optional[
            "capo_pinpoint_sms_voice_v2.types.notify_template_id.NotifyTemplateId"
        ] = None,
        time_to_live: Optional[
            "capo_pinpoint_sms_voice_v2.types.time_to_live.TimeToLive"
        ] = None,
        context: Optional[
            "capo_pinpoint_sms_voice_v2.types.context_map.ContextMap"
        ] = None,
        configuration_set_name: Optional[
            "capo_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn.ConfigurationSetNameOrArn"
        ] = None,
        dry_run: Optional[bool] = None,
        message_feedback_enabled: Optional[bool] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.send_notify_text_message_result.SendNotifyTextMessageResult":
        """<p>Sends a templated text message through a notify configuration to a recipient's phone number.</p>

        Args:
            notify_configuration_id: <p>The unique identifier of the notify configuration to use for sending the message. This can be either the NotifyConfigurationId or NotifyConfigurationArn.</p>
            destination_phone_number: <p>The destination phone number in E.164 format.</p>
            template_id: <p>The unique identifier of the template to use for the message.</p>
            template_variables: <p>A map of template variable names and their values. All variable values are passed as strings regardless of the declared variable type. For example, pass <code>INTEGER</code> values as <code>"42"</code> and <code>BOOLEAN</code> values as <code>"true"</code> or <code>"false"</code>.</p>
            time_to_live: <p>How long the text message is valid for, in seconds. By default this is 72 hours.</p>
            context: <p>You can specify custom data in this field. If you do, that data is logged to the event destination.</p>
            configuration_set_name: <p>The name of the configuration set to use. This can be either the ConfigurationSetName or ConfigurationSetArn.</p>
            dry_run: <p>When set to true, the message is checked and validated, but isn't sent to the end recipient.</p>
            message_feedback_enabled: <p>Set to true to enable message feedback for the message. When a user receives the message you need to update the message status using <a>PutMessageFeedback</a>.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            SendNotifyTextMessage
            Send an OTP verification code via SMS using a notify configuration.

            >>> await client.send_notify_text_message(notify_configuration_id='nc-1234567890abcdef0', destination_phone_number='+12065550100', template_variables={'code': '123456', 'expiry': '10'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.send_notify_text_message_request.SendNotifyTextMessageRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.send_notify_text_message_result.SendNotifyTextMessageResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.send_notify_text_message

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.send_notify_text_message.async_send_notify_text_message(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.send_notify_text_message_request.SendNotifyTextMessageRequest = {
            "notify_configuration_id": notify_configuration_id,
            "destination_phone_number": destination_phone_number,
            "template_variables": template_variables,
        }
        if template_id is not None:
            input_["template_id"] = template_id
        if time_to_live is not None:
            input_["time_to_live"] = time_to_live
        if context is not None:
            input_["context"] = context
        if configuration_set_name is not None:
            input_["configuration_set_name"] = configuration_set_name
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if message_feedback_enabled is not None:
            input_["message_feedback_enabled"] = message_feedback_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def send_notify_voice_message(
        self,
        notify_configuration_id: "capo_pinpoint_sms_voice_v2.types.notify_configuration_id_or_arn.NotifyConfigurationIdOrArn",
        destination_phone_number: "capo_pinpoint_sms_voice_v2.types.phone_number.PhoneNumber",
        template_variables: "capo_pinpoint_sms_voice_v2.types.template_variable_substitution_map.TemplateVariableSubstitutionMap",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        template_id: Optional[
            "capo_pinpoint_sms_voice_v2.types.notify_template_id.NotifyTemplateId"
        ] = None,
        voice_id: Optional["capo_pinpoint_sms_voice_v2.types.voice_id.VoiceId"] = None,
        time_to_live: Optional[
            "capo_pinpoint_sms_voice_v2.types.time_to_live.TimeToLive"
        ] = None,
        context: Optional[
            "capo_pinpoint_sms_voice_v2.types.context_map.ContextMap"
        ] = None,
        configuration_set_name: Optional[
            "capo_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn.ConfigurationSetNameOrArn"
        ] = None,
        dry_run: Optional[bool] = None,
        message_feedback_enabled: Optional[bool] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.send_notify_voice_message_result.SendNotifyVoiceMessageResult":
        """<p>Sends a templated voice message through a notify configuration to a recipient's phone number.</p>

        Args:
            notify_configuration_id: <p>The unique identifier of the notify configuration to use for sending the message. This can be either the NotifyConfigurationId or NotifyConfigurationArn.</p>
            destination_phone_number: <p>The destination phone number in E.164 format.</p>
            template_id: <p>The unique identifier of the template to use for the message.</p>
            template_variables: <p>A map of template variable names and their values. All variable values are passed as strings regardless of the declared variable type. For example, pass <code>INTEGER</code> values as <code>"42"</code> and <code>BOOLEAN</code> values as <code>"true"</code> or <code>"false"</code>.</p>
            voice_id: <p>The voice ID to use for the voice message.</p>
            time_to_live: <p>How long the voice message is valid for, in seconds. By default this is 72 hours.</p>
            context: <p>You can specify custom data in this field. If you do, that data is logged to the event destination.</p>
            configuration_set_name: <p>The name of the configuration set to use. This can be either the ConfigurationSetName or ConfigurationSetArn.</p>
            dry_run: <p>When set to true, the message is checked and validated, but isn't sent to the end recipient.</p>
            message_feedback_enabled: <p>Set to true to enable message feedback for the message. When a user receives the message you need to update the message status using <a>PutMessageFeedback</a>.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            SendNotifyVoiceMessage
            Send an OTP verification code via voice call using a notify configuration.

            >>> await client.send_notify_voice_message(notify_configuration_id='nc-1234567890abcdef0', destination_phone_number='+12065550100', template_variables={'code': '123456', 'expiry': '10'}, voice_id='JOANNA')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.send_notify_voice_message_request.SendNotifyVoiceMessageRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.send_notify_voice_message_result.SendNotifyVoiceMessageResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.send_notify_voice_message

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.send_notify_voice_message.async_send_notify_voice_message(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.send_notify_voice_message_request.SendNotifyVoiceMessageRequest = {
            "notify_configuration_id": notify_configuration_id,
            "destination_phone_number": destination_phone_number,
            "template_variables": template_variables,
        }
        if template_id is not None:
            input_["template_id"] = template_id
        if voice_id is not None:
            input_["voice_id"] = voice_id
        if time_to_live is not None:
            input_["time_to_live"] = time_to_live
        if context is not None:
            input_["context"] = context
        if configuration_set_name is not None:
            input_["configuration_set_name"] = configuration_set_name
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if message_feedback_enabled is not None:
            input_["message_feedback_enabled"] = message_feedback_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def send_rcs_message(
        self,
        destination_phone_number: "capo_pinpoint_sms_voice_v2.types.phone_number.PhoneNumber",
        origination_identity: "capo_pinpoint_sms_voice_v2.types.rcs_message_origination_identity.RcsMessageOriginationIdentity",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        rcs_message_content: Optional[
            "capo_pinpoint_sms_voice_v2.types.rcs_message_content.RcsMessageContent"
        ] = None,
        time_to_live: Optional[
            "capo_pinpoint_sms_voice_v2.types.rcs_time_to_live.RcsTimeToLive"
        ] = None,
        message_traffic_type: Optional[
            "capo_pinpoint_sms_voice_v2.types.rcs_message_traffic_type.RcsMessageTrafficType"
        ] = None,
        fallback_configuration: Optional[
            "capo_pinpoint_sms_voice_v2.types.rcs_fallback_configuration.RcsFallbackConfiguration"
        ] = None,
        protect_configuration_id: Optional[
            "capo_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn.ProtectConfigurationIdOrArn"
        ] = None,
        configuration_set_name: Optional[
            "capo_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn.ConfigurationSetNameOrArn"
        ] = None,
        max_price: Optional[
            "capo_pinpoint_sms_voice_v2.types.max_price.MaxPrice"
        ] = None,
        dry_run: Optional[bool] = None,
        context: Optional[
            "capo_pinpoint_sms_voice_v2.types.context_map.ContextMap"
        ] = None,
        message_feedback_enabled: Optional[bool] = None,
    ) -> (
        "capo_pinpoint_sms_voice_v2.types.send_rcs_message_result.SendRcsMessageResult"
    ):
        """<p>Creates a new RCS message and sends it to a recipient's phone number. RCS messages support rich content including text, files, rich cards, and carousels with interactive suggested actions.</p>

        Args:
            destination_phone_number: <p>The destination phone number in E.164 format.</p>
            origination_identity: <p>The origination identity of the message. This can be either the RcsAgentId, RcsAgentArn, PoolId, or PoolArn.</p>
            rcs_message_content: <p>The content of the RCS message. Contains the message content (text, file, rich card, or carousel) and optional message-level suggested actions.</p>
            time_to_live: <p>The duration in seconds that the RCS message is valid for delivery. If the message cannot be delivered within this duration, it is considered expired. Valid values are 1 to 172800 (48 hours). If a FallbackConfiguration is provided, the fallback is triggered when the duration expires without delivery confirmation.</p>
            message_traffic_type: <p>The traffic type of the RCS message. Valid values are AUTHENTICATION, TRANSACTION, PROMOTION, SERVICE_REQUEST, and ACKNOWLEDGEMENT. This field is reserved for future use.</p>
            fallback_configuration: <p>Configuration for SMS or MMS fallback when RCS delivery fails. If provided, the service sends a fallback message via the specified channel when the RCS message fails or the TimeToLive expires.</p>
            protect_configuration_id: <p>The unique identifier of the protect configuration to use.</p>
            configuration_set_name: <p>The name of the configuration set to use. This can be either the ConfigurationSetName or ConfigurationSetArn.</p>
            max_price: <p>The maximum amount that you want to spend, in US dollars, per each RCS message.</p>
            dry_run: <p>When set to true, the message is checked and validated, but isn't sent to the end recipient.</p>
            context: <p>You can specify custom data in this field. If you do, that data is logged to the event destination.</p>
            message_feedback_enabled: <p>Set to true to enable message feedback for the message. When a user receives the message you need to update the message status using <a>PutMessageFeedback</a>.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.send_rcs_message_request.SendRcsMessageRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.send_rcs_message_result.SendRcsMessageResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.send_rcs_message

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.send_rcs_message.async_send_rcs_message(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.send_rcs_message_request.SendRcsMessageRequest = {
            "destination_phone_number": destination_phone_number,
            "origination_identity": origination_identity,
        }
        if rcs_message_content is not None:
            input_["rcs_message_content"] = rcs_message_content
        if time_to_live is not None:
            input_["time_to_live"] = time_to_live
        if message_traffic_type is not None:
            input_["message_traffic_type"] = message_traffic_type
        if fallback_configuration is not None:
            input_["fallback_configuration"] = fallback_configuration
        if protect_configuration_id is not None:
            input_["protect_configuration_id"] = protect_configuration_id
        if configuration_set_name is not None:
            input_["configuration_set_name"] = configuration_set_name
        if max_price is not None:
            input_["max_price"] = max_price
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if context is not None:
            input_["context"] = context
        if message_feedback_enabled is not None:
            input_["message_feedback_enabled"] = message_feedback_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def send_text_message(
        self,
        destination_phone_number: "capo_pinpoint_sms_voice_v2.types.phone_number.PhoneNumber",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        origination_identity: Optional[
            "capo_pinpoint_sms_voice_v2.types.text_message_origination_identity.TextMessageOriginationIdentity"
        ] = None,
        message_body: Optional[
            "capo_pinpoint_sms_voice_v2.types.text_message_body.TextMessageBody"
        ] = None,
        message_type: Optional[
            "capo_pinpoint_sms_voice_v2.types.message_type.MessageType"
        ] = None,
        keyword: Optional["capo_pinpoint_sms_voice_v2.types.keyword.Keyword"] = None,
        configuration_set_name: Optional[
            "capo_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn.ConfigurationSetNameOrArn"
        ] = None,
        max_price: Optional[
            "capo_pinpoint_sms_voice_v2.types.max_price.MaxPrice"
        ] = None,
        time_to_live: Optional[
            "capo_pinpoint_sms_voice_v2.types.time_to_live.TimeToLive"
        ] = None,
        context: Optional[
            "capo_pinpoint_sms_voice_v2.types.context_map.ContextMap"
        ] = None,
        destination_country_parameters: Optional[
            "capo_pinpoint_sms_voice_v2.types.destination_country_parameters.DestinationCountryParameters"
        ] = None,
        dry_run: Optional[bool] = None,
        protect_configuration_id: Optional[
            "capo_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn.ProtectConfigurationIdOrArn"
        ] = None,
        message_feedback_enabled: Optional[bool] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.send_text_message_result.SendTextMessageResult":
        """<p>Creates a new text message and sends it to a recipient's phone number. SendTextMessage only sends an SMS message to one recipient each time it is invoked.</p> <p>SMS throughput limits are measured in Message Parts per Second (MPS). Your MPS limit depends on the destination country of your messages, as well as the type of phone number (origination number) that you use to send the message. For more information about MPS, see <a href="https://docs.aws.amazon.com/sms-voice/latest/userguide/sms-limitations-mps.html">Message Parts per Second (MPS) limits</a> in the <i>End User Messaging SMS User Guide</i>.</p>

        Args:
            destination_phone_number: <p>The destination phone number in E.164 format.</p>
            origination_identity: <p>The origination identity of the message. This can be either the PhoneNumber, PhoneNumberId, PhoneNumberArn, RcsAgentId, RcsAgentArn, SenderId, SenderIdArn, PoolId, or PoolArn.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>
            message_body: <p>The body of the text message.</p>
            message_type: <p>The type of message. Valid values are for messages that are critical or time-sensitive and PROMOTIONAL for messages that aren't critical or time-sensitive.</p>
            keyword: <p>When you register a short code in the US, you must specify a program name. If you don’t have a US short code, omit this attribute.</p>
            configuration_set_name: <p>The name of the configuration set to use. This can be either the ConfigurationSetName or ConfigurationSetArn.</p>
            max_price: <p>The maximum amount that you want to spend, in US dollars, per each text message. If the calculated amount to send the text message is greater than <code>MaxPrice</code>, the message is not sent and an error is returned.</p>
            time_to_live: <p>How long the text message is valid for, in seconds. By default this is 72 hours. If the messages isn't handed off before the TTL expires we stop attempting to hand off the message and return <code>TTL_EXPIRED</code> event.</p>
            context: <p>You can specify custom data in this field. If you do, that data is logged to the event destination.</p>
            destination_country_parameters: <p>This field is used for any country-specific registration requirements. Currently, this setting is only used when you send messages to recipients in India using a sender ID. For more information see <a href="https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms-senderid-india.html">Special requirements for sending SMS messages to recipients in India</a>. </p> <ul> <li> <p> <code>IN_ENTITY_ID</code> The entity ID or Principal Entity (PE) ID that you received after completing the sender ID registration process.</p> </li> <li> <p> <code>IN_TEMPLATE_ID</code> The template ID that you received after completing the sender ID registration process.</p> <important> <p>Make sure that the Template ID that you specify matches your message template exactly. If your message doesn't match the template that you provided during the registration process, the mobile carriers might reject your message.</p> </important> </li> </ul>
            dry_run: <p>When set to true, the message is checked and validated, but isn't sent to the end recipient. You are not charged for using <code>DryRun</code>.</p> <p>The Message Parts per Second (MPS) limit when using <code>DryRun</code> is five. If your origination identity has a lower MPS limit then the lower MPS limit is used. For more information about MPS limits, see <a href="https://docs.aws.amazon.com/sms-voice/latest/userguide/sms-limitations-mps.html">Message Parts per Second (MPS) limits</a> in the <i>End User Messaging SMS User Guide</i>..</p>
            protect_configuration_id: <p>The unique identifier for the protect configuration.</p>
            message_feedback_enabled: <p>Set to true to enable message feedback for the message. When a user receives the message you need to update the message status using <a>PutMessageFeedback</a>.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.send_text_message_request.SendTextMessageRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.send_text_message_result.SendTextMessageResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.send_text_message

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.send_text_message.async_send_text_message(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.send_text_message_request.SendTextMessageRequest = {
            "destination_phone_number": destination_phone_number
        }
        if origination_identity is not None:
            input_["origination_identity"] = origination_identity
        if message_body is not None:
            input_["message_body"] = message_body
        if message_type is not None:
            input_["message_type"] = message_type
        if keyword is not None:
            input_["keyword"] = keyword
        if configuration_set_name is not None:
            input_["configuration_set_name"] = configuration_set_name
        if max_price is not None:
            input_["max_price"] = max_price
        if time_to_live is not None:
            input_["time_to_live"] = time_to_live
        if context is not None:
            input_["context"] = context
        if destination_country_parameters is not None:
            input_["destination_country_parameters"] = destination_country_parameters
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if protect_configuration_id is not None:
            input_["protect_configuration_id"] = protect_configuration_id
        if message_feedback_enabled is not None:
            input_["message_feedback_enabled"] = message_feedback_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def send_voice_message(
        self,
        destination_phone_number: "capo_pinpoint_sms_voice_v2.types.phone_number.PhoneNumber",
        origination_identity: "capo_pinpoint_sms_voice_v2.types.voice_message_origination_identity.VoiceMessageOriginationIdentity",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        message_body: Optional[
            "capo_pinpoint_sms_voice_v2.types.voice_message_body.VoiceMessageBody"
        ] = None,
        message_body_text_type: Optional[
            "capo_pinpoint_sms_voice_v2.types.voice_message_body_text_type.VoiceMessageBodyTextType"
        ] = None,
        voice_id: Optional["capo_pinpoint_sms_voice_v2.types.voice_id.VoiceId"] = None,
        configuration_set_name: Optional[
            "capo_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn.ConfigurationSetNameOrArn"
        ] = None,
        max_price_per_minute: Optional[
            "capo_pinpoint_sms_voice_v2.types.max_price.MaxPrice"
        ] = None,
        time_to_live: Optional[
            "capo_pinpoint_sms_voice_v2.types.time_to_live.TimeToLive"
        ] = None,
        context: Optional[
            "capo_pinpoint_sms_voice_v2.types.context_map.ContextMap"
        ] = None,
        dry_run: Optional[bool] = None,
        protect_configuration_id: Optional[
            "capo_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn.ProtectConfigurationIdOrArn"
        ] = None,
        message_feedback_enabled: Optional[bool] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.send_voice_message_result.SendVoiceMessageResult":
        """<p>Allows you to send a request that sends a voice message. This operation uses <a href="http://aws.amazon.com/polly/">Amazon Polly</a> to convert a text script into a voice message.</p>

        Args:
            destination_phone_number: <p>The destination phone number in E.164 format.</p>
            origination_identity: <p>The origination identity to use for the voice call. This can be the PhoneNumber, PhoneNumberId, PhoneNumberArn, PoolId, or PoolArn.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>
            message_body: <p>The text to convert to a voice message.</p>
            message_body_text_type: <p>Specifies if the MessageBody field contains text or <a href="https://docs.aws.amazon.com/polly/latest/dg/what-is.html">speech synthesis markup language (SSML)</a>.</p> <ul> <li> <p>TEXT: This is the default value. When used the maximum character limit is 3000.</p> </li> <li> <p>SSML: When used the maximum character limit is 6000 including SSML tagging.</p> </li> </ul>
            voice_id: <p>The voice for the <a href="https://docs.aws.amazon.com/polly/latest/dg/what-is.html">Amazon Polly</a> service to use. By default this is set to "MATTHEW".</p>
            configuration_set_name: <p>The name of the configuration set to use. This can be either the ConfigurationSetName or ConfigurationSetArn.</p>
            max_price_per_minute: <p>The maximum amount to spend per voice message, in US dollars.</p>
            time_to_live: <p>How long the voice message is valid for. By default this is 72 hours.</p>
            context: <p>You can specify custom data in this field. If you do, that data is logged to the event destination.</p>
            dry_run: <p>When set to true, the message is checked and validated, but isn't sent to the end recipient.</p>
            protect_configuration_id: <p>The unique identifier for the protect configuration.</p>
            message_feedback_enabled: <p>Set to true to enable message feedback for the message. When a user receives the message you need to update the message status using <a>PutMessageFeedback</a>.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.send_voice_message_request.SendVoiceMessageRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.send_voice_message_result.SendVoiceMessageResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.send_voice_message

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.send_voice_message.async_send_voice_message(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.send_voice_message_request.SendVoiceMessageRequest = {
            "destination_phone_number": destination_phone_number,
            "origination_identity": origination_identity,
        }
        if message_body is not None:
            input_["message_body"] = message_body
        if message_body_text_type is not None:
            input_["message_body_text_type"] = message_body_text_type
        if voice_id is not None:
            input_["voice_id"] = voice_id
        if configuration_set_name is not None:
            input_["configuration_set_name"] = configuration_set_name
        if max_price_per_minute is not None:
            input_["max_price_per_minute"] = max_price_per_minute
        if time_to_live is not None:
            input_["time_to_live"] = time_to_live
        if context is not None:
            input_["context"] = context
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if protect_configuration_id is not None:
            input_["protect_configuration_id"] = protect_configuration_id
        if message_feedback_enabled is not None:
            input_["message_feedback_enabled"] = message_feedback_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def set_account_default_protect_configuration(
        self,
        protect_configuration_id: "capo_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn.ProtectConfigurationIdOrArn",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.set_account_default_protect_configuration_result.SetAccountDefaultProtectConfigurationResult":
        """<p>Set a protect configuration as your account default. You can only have one account default protect configuration at a time. The current account default protect configuration is replaced with the provided protect configuration.</p>

        Args:
            protect_configuration_id: <p>The unique identifier for the protect configuration.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.set_account_default_protect_configuration_request.SetAccountDefaultProtectConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.set_account_default_protect_configuration_result.SetAccountDefaultProtectConfigurationResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.set_account_default_protect_configuration

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.set_account_default_protect_configuration.async_set_account_default_protect_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.set_account_default_protect_configuration_request.SetAccountDefaultProtectConfigurationRequest = {
            "protect_configuration_id": protect_configuration_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def set_default_message_feedback_enabled(
        self,
        configuration_set_name: "capo_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn.ConfigurationSetNameOrArn",
        message_feedback_enabled: bool,
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.set_default_message_feedback_enabled_result.SetDefaultMessageFeedbackEnabledResult":
        """<p>Sets a configuration set's default for message feedback. </p>

        Args:
            configuration_set_name: <p>The name of the configuration set to use. This can be either the ConfigurationSetName or ConfigurationSetArn.</p>
            message_feedback_enabled: <p>Set to true to enable message feedback.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.set_default_message_feedback_enabled_request.SetDefaultMessageFeedbackEnabledRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.set_default_message_feedback_enabled_result.SetDefaultMessageFeedbackEnabledResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.set_default_message_feedback_enabled

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.set_default_message_feedback_enabled.async_set_default_message_feedback_enabled(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.set_default_message_feedback_enabled_request.SetDefaultMessageFeedbackEnabledRequest = {
            "configuration_set_name": configuration_set_name,
            "message_feedback_enabled": message_feedback_enabled,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def set_default_message_type(
        self,
        configuration_set_name: "capo_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn.ConfigurationSetNameOrArn",
        message_type: "capo_pinpoint_sms_voice_v2.types.message_type.MessageType",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.set_default_message_type_result.SetDefaultMessageTypeResult":
        """<p>Sets the default message type on a configuration set.</p> <p>Choose the category of SMS messages that you plan to send from this account. If you send account-related messages or time-sensitive messages such as one-time passcodes, choose <b>Transactional</b>. If you plan to send messages that contain marketing material or other promotional content, choose <b>Promotional</b>. This setting applies to your entire Amazon Web Services account.</p>

        Args:
            configuration_set_name: <p>The configuration set to update with a new default message type. This field can be the ConsigurationSetName or ConfigurationSetArn.</p>
            message_type: <p>The type of message. Valid values are TRANSACTIONAL for messages that are critical or time-sensitive and PROMOTIONAL for messages that aren't critical or time-sensitive.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.set_default_message_type_request.SetDefaultMessageTypeRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.set_default_message_type_result.SetDefaultMessageTypeResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.set_default_message_type

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.set_default_message_type.async_set_default_message_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.set_default_message_type_request.SetDefaultMessageTypeRequest = {
            "configuration_set_name": configuration_set_name,
            "message_type": message_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def set_default_sender_id(
        self,
        configuration_set_name: "capo_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn.ConfigurationSetNameOrArn",
        sender_id: "capo_pinpoint_sms_voice_v2.types.sender_id.SenderId",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.set_default_sender_id_result.SetDefaultSenderIdResult":
        """<p>Sets default sender ID on a configuration set.</p> <p>When sending a text message to a destination country that supports sender IDs, the default sender ID on the configuration set specified will be used if no dedicated origination phone numbers or registered sender IDs are available in your account.</p>

        Args:
            configuration_set_name: <p>The configuration set to updated with a new default SenderId. This field can be the ConsigurationSetName or ConfigurationSetArn.</p>
            sender_id: <p>The current sender ID for the configuration set. When sending a text message to a destination country which supports SenderIds, the default sender ID on the configuration set specified on <a>SendTextMessage</a> will be used if no dedicated origination phone numbers or registered SenderIds are available in your account, instead of a generic sender ID, such as 'NOTICE'.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.set_default_sender_id_request.SetDefaultSenderIdRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.set_default_sender_id_result.SetDefaultSenderIdResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.set_default_sender_id

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.set_default_sender_id.async_set_default_sender_id(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.set_default_sender_id_request.SetDefaultSenderIdRequest = {
            "configuration_set_name": configuration_set_name,
            "sender_id": sender_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def set_media_message_spend_limit_override(
        self,
        monthly_limit: "capo_pinpoint_sms_voice_v2.types.monthly_limit.MonthlyLimit",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.set_media_message_spend_limit_override_result.SetMediaMessageSpendLimitOverrideResult":
        """<p>Sets an account level monthly spend limit override for sending MMS messages. The requested spend limit must be less than or equal to the <code>MaxLimit</code>, which is set by Amazon Web Services. </p>

        Args:
            monthly_limit: <p>The new monthly limit to enforce on text messages.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.set_media_message_spend_limit_override_request.SetMediaMessageSpendLimitOverrideRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.set_media_message_spend_limit_override_result.SetMediaMessageSpendLimitOverrideResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.set_media_message_spend_limit_override

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.set_media_message_spend_limit_override.async_set_media_message_spend_limit_override(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.set_media_message_spend_limit_override_request.SetMediaMessageSpendLimitOverrideRequest = {
            "monthly_limit": monthly_limit
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def set_notify_message_spend_limit_override(
        self,
        monthly_limit: "capo_pinpoint_sms_voice_v2.types.monthly_limit.MonthlyLimit",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.set_notify_message_spend_limit_override_result.SetNotifyMessageSpendLimitOverrideResult":
        """<p>Sets an account level monthly spend limit override for sending notify messages. The requested spend limit must be less than or equal to the <code>MaxLimit</code>, which is set by Amazon Web Services. </p>

        Args:
            monthly_limit: <p>The new monthly limit to enforce on notify messages.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            SetNotifyMessageSpendLimitOverride
            Set a monthly spend limit override for notify messages.

            >>> await client.set_notify_message_spend_limit_override(monthly_limit=1000)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.set_notify_message_spend_limit_override_request.SetNotifyMessageSpendLimitOverrideRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.set_notify_message_spend_limit_override_result.SetNotifyMessageSpendLimitOverrideResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.set_notify_message_spend_limit_override

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.set_notify_message_spend_limit_override.async_set_notify_message_spend_limit_override(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.set_notify_message_spend_limit_override_request.SetNotifyMessageSpendLimitOverrideRequest = {
            "monthly_limit": monthly_limit
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def set_rcs_message_spend_limit_override(
        self,
        monthly_limit: "capo_pinpoint_sms_voice_v2.types.monthly_limit.MonthlyLimit",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.set_rcs_message_spend_limit_override_result.SetRcsMessageSpendLimitOverrideResult":
        """<p>Sets an account level monthly spend limit override for sending RCS messages. The requested spend limit must be less than or equal to the <code>MaxLimit</code>, which is set by Amazon Web Services.</p>

        Args:
            monthly_limit: <p>The new monthly limit to enforce on RCS message spending.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.set_rcs_message_spend_limit_override_request.SetRcsMessageSpendLimitOverrideRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.set_rcs_message_spend_limit_override_result.SetRcsMessageSpendLimitOverrideResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.set_rcs_message_spend_limit_override

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.set_rcs_message_spend_limit_override.async_set_rcs_message_spend_limit_override(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.set_rcs_message_spend_limit_override_request.SetRcsMessageSpendLimitOverrideRequest = {
            "monthly_limit": monthly_limit
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def set_text_message_spend_limit_override(
        self,
        monthly_limit: "capo_pinpoint_sms_voice_v2.types.monthly_limit.MonthlyLimit",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.set_text_message_spend_limit_override_result.SetTextMessageSpendLimitOverrideResult":
        """<p>Sets an account level monthly spend limit override for sending text messages. The requested spend limit must be less than or equal to the <code>MaxLimit</code>, which is set by Amazon Web Services. </p>

        Args:
            monthly_limit: <p>The new monthly limit to enforce on text messages.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.set_text_message_spend_limit_override_request.SetTextMessageSpendLimitOverrideRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.set_text_message_spend_limit_override_result.SetTextMessageSpendLimitOverrideResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.set_text_message_spend_limit_override

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.set_text_message_spend_limit_override.async_set_text_message_spend_limit_override(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.set_text_message_spend_limit_override_request.SetTextMessageSpendLimitOverrideRequest = {
            "monthly_limit": monthly_limit
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def set_voice_message_spend_limit_override(
        self,
        monthly_limit: "capo_pinpoint_sms_voice_v2.types.monthly_limit.MonthlyLimit",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.set_voice_message_spend_limit_override_result.SetVoiceMessageSpendLimitOverrideResult":
        """<p>Sets an account level monthly spend limit override for sending voice messages. The requested spend limit must be less than or equal to the <code>MaxLimit</code>, which is set by Amazon Web Services. </p>

        Args:
            monthly_limit: <p>The new monthly limit to enforce on voice messages.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.set_voice_message_spend_limit_override_request.SetVoiceMessageSpendLimitOverrideRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.set_voice_message_spend_limit_override_result.SetVoiceMessageSpendLimitOverrideResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.set_voice_message_spend_limit_override

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.set_voice_message_spend_limit_override.async_set_voice_message_spend_limit_override(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.set_voice_message_spend_limit_override_request.SetVoiceMessageSpendLimitOverrideRequest = {
            "monthly_limit": monthly_limit
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def submit_registration_version(
        self,
        registration_id: "capo_pinpoint_sms_voice_v2.types.registration_id_or_arn.RegistrationIdOrArn",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        aws_review: Optional[bool] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.submit_registration_version_result.SubmitRegistrationVersionResult":
        """<p>Submit the specified registration for review and approval.</p>

        Args:
            registration_id: <p>The unique identifier for the registration.</p>
            aws_review: <p>Set to true to request AWS review of the registration. When enabled, AWS will perform additional validation and review of the registration submission before processing.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.submit_registration_version_request.SubmitRegistrationVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.submit_registration_version_result.SubmitRegistrationVersionResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.submit_registration_version

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.submit_registration_version.async_submit_registration_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.submit_registration_version_request.SubmitRegistrationVersionRequest = {
            "registration_id": registration_id
        }
        if aws_review is not None:
            input_["aws_review"] = aws_review

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_pinpoint_sms_voice_v2.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_pinpoint_sms_voice_v2.types.non_empty_tag_list.NonEmptyTagList",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.tag_resource_result.TagResourceResult":
        """<p>Adds or overwrites only the specified tags for the specified resource. When you specify an existing tag key, the value is overwritten with the new value. Each tag consists of a key and an optional value. Tag keys must be unique per resource. For more information about tags, see <a href="https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-tags.html">Tags </a> in the <i>End User Messaging SMS User Guide</i>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tags: <p>An array of key and value pair tags that are associated with the resource.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.tag_resource_result.TagResourceResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.tag_resource

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_pinpoint_sms_voice_v2.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_pinpoint_sms_voice_v2.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.untag_resource_result.UntagResourceResult":
        """<p>Removes the association of the specified tags from a resource. For more information on tags see <a href="https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-tags.html">Tags </a> in the <i>End User Messaging SMS User Guide</i>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>An array of tag key values to unassociate with the resource.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.untag_resource_result.UntagResourceResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.untag_resource

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.untag_resource_request.UntagResourceRequest = {
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

    async def update_event_destination(
        self,
        configuration_set_name: "capo_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn.ConfigurationSetNameOrArn",
        event_destination_name: "capo_pinpoint_sms_voice_v2.types.event_destination_name.EventDestinationName",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        enabled: Optional[bool] = None,
        matching_event_types: Optional[
            "capo_pinpoint_sms_voice_v2.types.event_type_list.EventTypeList"
        ] = None,
        cloud_watch_logs_destination: Optional[
            "capo_pinpoint_sms_voice_v2.types.cloud_watch_logs_destination.CloudWatchLogsDestination"
        ] = None,
        kinesis_firehose_destination: Optional[
            "capo_pinpoint_sms_voice_v2.types.kinesis_firehose_destination.KinesisFirehoseDestination"
        ] = None,
        sns_destination: Optional[
            "capo_pinpoint_sms_voice_v2.types.sns_destination.SnsDestination"
        ] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.update_event_destination_result.UpdateEventDestinationResult":
        """<p>Updates an existing event destination in a configuration set. You can update the IAM role ARN for CloudWatch Logs and Firehose. You can also enable or disable the event destination.</p> <p>You may want to update an event destination to change its matching event types or updating the destination resource ARN. You can't change an event destination's type between CloudWatch Logs, Firehose, and Amazon SNS.</p>

        Args:
            configuration_set_name: <p>The configuration set to update with the new event destination. Valid values for this can be the ConfigurationSetName or ConfigurationSetArn.</p>
            event_destination_name: <p>The name to use for the event destination.</p>
            enabled: <p>When set to true logging is enabled.</p>
            matching_event_types: <p>An array of event types that determine which events to log.</p> <note> <p>The <code>TEXT_SENT</code> event type is not supported.</p> </note>
            cloud_watch_logs_destination: <p>An object that contains information about an event destination that sends data to CloudWatch Logs.</p>
            kinesis_firehose_destination: <p>An object that contains information about an event destination for logging to Firehose.</p>
            sns_destination: <p>An object that contains information about an event destination that sends data to Amazon SNS.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.update_event_destination_request.UpdateEventDestinationRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.update_event_destination_result.UpdateEventDestinationResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.update_event_destination

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.update_event_destination.async_update_event_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.update_event_destination_request.UpdateEventDestinationRequest = {
            "configuration_set_name": configuration_set_name,
            "event_destination_name": event_destination_name,
        }
        if enabled is not None:
            input_["enabled"] = enabled
        if matching_event_types is not None:
            input_["matching_event_types"] = matching_event_types
        if cloud_watch_logs_destination is not None:
            input_["cloud_watch_logs_destination"] = cloud_watch_logs_destination
        if kinesis_firehose_destination is not None:
            input_["kinesis_firehose_destination"] = kinesis_firehose_destination
        if sns_destination is not None:
            input_["sns_destination"] = sns_destination

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_notify_configuration(
        self,
        notify_configuration_id: "capo_pinpoint_sms_voice_v2.types.notify_configuration_id_or_arn.NotifyConfigurationIdOrArn",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        default_template_id: Optional[
            "capo_pinpoint_sms_voice_v2.types.notify_template_id.NotifyTemplateId"
        ] = None,
        pool_id: Optional[
            "capo_pinpoint_sms_voice_v2.types.notify_pool_id_or_unset.NotifyPoolIdOrUnset"
        ] = None,
        enabled_countries: Optional[
            "capo_pinpoint_sms_voice_v2.types.iso_country_code_list.IsoCountryCodeList"
        ] = None,
        enabled_channels: Optional[
            "capo_pinpoint_sms_voice_v2.types.notify_enabled_channels_list.NotifyEnabledChannelsList"
        ] = None,
        deletion_protection_enabled: Optional[bool] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.update_notify_configuration_result.UpdateNotifyConfigurationResult":
        """<p>Updates an existing notify configuration. You can update the default template, pool association, enabled channels, enabled countries, and deletion protection settings.</p>

        Args:
            notify_configuration_id: <p>The identifier of the notify configuration to update. The NotifyConfigurationId can be found using the <a>DescribeNotifyConfigurations</a> operation.</p>
            default_template_id: <p>The default template identifier to associate with the notify configuration. If specified, this template is used when sending messages without an explicit template identifier. Pass the special value <code>UNSET_DEFAULT_TEMPLATE</code> to clear the current default template from the notify configuration.</p>
            pool_id: <p>The pool identifier or Amazon Resource Name (ARN) to associate with the notify configuration. Pass the special value <code>UNSET_DEFAULT_POOL_FOR_NOTIFY</code> to clear the current default pool from the notify configuration.</p>
            enabled_countries: <p>An array of two-character ISO country codes, in ISO 3166-1 alpha-2 format, that are enabled for the notify configuration.</p>
            enabled_channels: <p>An array of channels to enable for the notify configuration. Supported values include <code>SMS</code> and <code>VOICE</code>.</p>
            deletion_protection_enabled: <p>When set to true the notify configuration can't be deleted.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            UpdateNotifyConfiguration
            Update a notify configuration to add voice channel and additional countries.

            >>> await client.update_notify_configuration(notify_configuration_id='nc-1234567890abcdef0', enabled_channels=['SMS', 'VOICE'], enabled_countries=['US', 'CA', 'GB'], deletion_protection_enabled=True)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.update_notify_configuration_request.UpdateNotifyConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.update_notify_configuration_result.UpdateNotifyConfigurationResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.update_notify_configuration

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.update_notify_configuration.async_update_notify_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.update_notify_configuration_request.UpdateNotifyConfigurationRequest = {
            "notify_configuration_id": notify_configuration_id
        }
        if default_template_id is not None:
            input_["default_template_id"] = default_template_id
        if pool_id is not None:
            input_["pool_id"] = pool_id
        if enabled_countries is not None:
            input_["enabled_countries"] = enabled_countries
        if enabled_channels is not None:
            input_["enabled_channels"] = enabled_channels
        if deletion_protection_enabled is not None:
            input_["deletion_protection_enabled"] = deletion_protection_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_phone_number(
        self,
        phone_number_id: "capo_pinpoint_sms_voice_v2.types.phone_number_id_or_arn.PhoneNumberIdOrArn",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        two_way_enabled: Optional[bool] = None,
        two_way_channel_arn: Optional[
            "capo_pinpoint_sms_voice_v2.types.two_way_channel_arn.TwoWayChannelArn"
        ] = None,
        two_way_channel_role: Optional[
            "capo_pinpoint_sms_voice_v2.types.iam_role_arn.IamRoleArn"
        ] = None,
        self_managed_opt_outs_enabled: Optional[bool] = None,
        opt_out_list_name: Optional[
            "capo_pinpoint_sms_voice_v2.types.opt_out_list_name_or_arn.OptOutListNameOrArn"
        ] = None,
        international_sending_enabled: Optional[bool] = None,
        deletion_protection_enabled: Optional[bool] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.update_phone_number_result.UpdatePhoneNumberResult":
        """<p>Updates the configuration of an existing origination phone number. You can update the opt-out list, enable or disable two-way messaging, change the TwoWayChannelArn, enable or disable self-managed opt-outs, and enable or disable deletion protection.</p> <p>If the origination phone number is associated with a pool, an error is returned.</p>

        Args:
            phone_number_id: <p>The unique identifier of the phone number. Valid values for this field can be either the PhoneNumberId or PhoneNumberArn.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>
            two_way_enabled: <p>By default this is set to false. When set to true you can receive incoming text messages from your end recipients.</p>
            two_way_channel_arn: <p>The Amazon Resource Name (ARN) of the two way channel.</p>
            two_way_channel_role: <p>An optional IAM Role Arn for a service to assume, to be able to post inbound SMS messages.</p>
            self_managed_opt_outs_enabled: <p>By default this is set to false. When set to false and an end recipient sends a message that begins with HELP or STOP to one of your dedicated numbers, End User Messaging SMS automatically replies with a customizable message and adds the end recipient to the OptOutList. When set to true you're responsible for responding to HELP and STOP requests. You're also responsible for tracking and honoring opt-out requests.</p>
            opt_out_list_name: <p>The OptOutList to add the phone number to. You can use either the opt out list name or the opt out list ARN.</p>
            international_sending_enabled: <p>By default this is set to false. When set to true the international sending of phone number is Enabled. </p>
            deletion_protection_enabled: <p>By default this is set to false. When set to true the phone number can't be deleted. </p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.update_phone_number_request.UpdatePhoneNumberRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.update_phone_number_result.UpdatePhoneNumberResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.update_phone_number

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.update_phone_number.async_update_phone_number(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.update_phone_number_request.UpdatePhoneNumberRequest = {
            "phone_number_id": phone_number_id
        }
        if two_way_enabled is not None:
            input_["two_way_enabled"] = two_way_enabled
        if two_way_channel_arn is not None:
            input_["two_way_channel_arn"] = two_way_channel_arn
        if two_way_channel_role is not None:
            input_["two_way_channel_role"] = two_way_channel_role
        if self_managed_opt_outs_enabled is not None:
            input_["self_managed_opt_outs_enabled"] = self_managed_opt_outs_enabled
        if opt_out_list_name is not None:
            input_["opt_out_list_name"] = opt_out_list_name
        if international_sending_enabled is not None:
            input_["international_sending_enabled"] = international_sending_enabled
        if deletion_protection_enabled is not None:
            input_["deletion_protection_enabled"] = deletion_protection_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_pool(
        self,
        pool_id: "capo_pinpoint_sms_voice_v2.types.pool_id_or_arn.PoolIdOrArn",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        two_way_enabled: Optional[bool] = None,
        two_way_channel_arn: Optional[
            "capo_pinpoint_sms_voice_v2.types.two_way_channel_arn.TwoWayChannelArn"
        ] = None,
        two_way_channel_role: Optional[
            "capo_pinpoint_sms_voice_v2.types.iam_role_arn.IamRoleArn"
        ] = None,
        self_managed_opt_outs_enabled: Optional[bool] = None,
        opt_out_list_name: Optional[
            "capo_pinpoint_sms_voice_v2.types.opt_out_list_name_or_arn.OptOutListNameOrArn"
        ] = None,
        shared_routes_enabled: Optional[bool] = None,
        deletion_protection_enabled: Optional[bool] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.update_pool_result.UpdatePoolResult":
        """<p>Updates the configuration of an existing pool. You can update the opt-out list, enable or disable two-way messaging, change the <code>TwoWayChannelArn</code>, enable or disable self-managed opt-outs, enable or disable deletion protection, and enable or disable shared routes.</p>

        Args:
            pool_id: <p>The unique identifier of the pool to update. Valid values are either the PoolId or PoolArn.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>
            two_way_enabled: <p>By default this is set to false. When set to true you can receive incoming text messages from your end recipients.</p>
            two_way_channel_arn: <p>The Amazon Resource Name (ARN) of the two way channel.</p>
            two_way_channel_role: <p>An optional IAM Role Arn for a service to assume, to be able to post inbound SMS messages.</p>
            self_managed_opt_outs_enabled: <p>By default this is set to false. When set to false and an end recipient sends a message that begins with HELP or STOP to one of your dedicated numbers, End User Messaging SMS automatically replies with a customizable message and adds the end recipient to the OptOutList. When set to true you're responsible for responding to HELP and STOP requests. You're also responsible for tracking and honoring opt-out requests.</p>
            opt_out_list_name: <p>The OptOutList to associate with the pool. Valid values are either OptOutListName or OptOutListArn.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>
            shared_routes_enabled: <p>Indicates whether shared routes are enabled for the pool.</p>
            deletion_protection_enabled: <p>When set to true the pool can't be deleted.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.update_pool_request.UpdatePoolRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.update_pool_result.UpdatePoolResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.update_pool

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.update_pool.async_update_pool(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.update_pool_request.UpdatePoolRequest = {
            "pool_id": pool_id
        }
        if two_way_enabled is not None:
            input_["two_way_enabled"] = two_way_enabled
        if two_way_channel_arn is not None:
            input_["two_way_channel_arn"] = two_way_channel_arn
        if two_way_channel_role is not None:
            input_["two_way_channel_role"] = two_way_channel_role
        if self_managed_opt_outs_enabled is not None:
            input_["self_managed_opt_outs_enabled"] = self_managed_opt_outs_enabled
        if opt_out_list_name is not None:
            input_["opt_out_list_name"] = opt_out_list_name
        if shared_routes_enabled is not None:
            input_["shared_routes_enabled"] = shared_routes_enabled
        if deletion_protection_enabled is not None:
            input_["deletion_protection_enabled"] = deletion_protection_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_protect_configuration(
        self,
        protect_configuration_id: "capo_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn.ProtectConfigurationIdOrArn",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        deletion_protection_enabled: Optional[bool] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.update_protect_configuration_result.UpdateProtectConfigurationResult":
        """<p>Update the setting for an existing protect configuration.</p>

        Args:
            protect_configuration_id: <p>The unique identifier for the protect configuration.</p>
            deletion_protection_enabled: <p>When set to true deletion protection is enabled. By default this is set to false. </p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.update_protect_configuration_request.UpdateProtectConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.update_protect_configuration_result.UpdateProtectConfigurationResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.update_protect_configuration

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.update_protect_configuration.async_update_protect_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.update_protect_configuration_request.UpdateProtectConfigurationRequest = {
            "protect_configuration_id": protect_configuration_id
        }
        if deletion_protection_enabled is not None:
            input_["deletion_protection_enabled"] = deletion_protection_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_protect_configuration_country_rule_set(
        self,
        protect_configuration_id: "capo_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn.ProtectConfigurationIdOrArn",
        number_capability: "capo_pinpoint_sms_voice_v2.types.number_capability.NumberCapability",
        country_rule_set_updates: "capo_pinpoint_sms_voice_v2.types.protect_configuration_country_rule_set.ProtectConfigurationCountryRuleSet",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.update_protect_configuration_country_rule_set_result.UpdateProtectConfigurationCountryRuleSetResult":
        """<p>Update a country rule set to <code>ALLOW</code>, <code>BLOCK</code>, <code>MONITOR</code>, or <code>FILTER</code> messages to be sent to the specified destination counties. You can update one or multiple countries at a time. The updates are only applied to the specified NumberCapability type.</p>

        Args:
            protect_configuration_id: <p>The unique identifier for the protect configuration.</p>
            number_capability: <p>The number capability to apply the CountryRuleSetUpdates updates to.</p>
            country_rule_set_updates: <p>A map of ProtectConfigurationCountryRuleSetInformation objects that contain the details for the requested NumberCapability. The Key is the two-letter ISO country code. For a list of supported ISO country codes, see <a href="https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-sms-by-country.html">Supported countries and regions (SMS channel)</a> in the End User Messaging SMS User Guide.</p> <p>For example, to set the United States as allowed and Canada as blocked, the <code>CountryRuleSetUpdates</code> would be formatted as: <code>"CountryRuleSetUpdates": { "US" : { "ProtectStatus": "ALLOW" } "CA" : { "ProtectStatus": "BLOCK" } }</code> </p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.update_protect_configuration_country_rule_set_request.UpdateProtectConfigurationCountryRuleSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.update_protect_configuration_country_rule_set_result.UpdateProtectConfigurationCountryRuleSetResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.update_protect_configuration_country_rule_set

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.update_protect_configuration_country_rule_set.async_update_protect_configuration_country_rule_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.update_protect_configuration_country_rule_set_request.UpdateProtectConfigurationCountryRuleSetRequest = {
            "protect_configuration_id": protect_configuration_id,
            "number_capability": number_capability,
            "country_rule_set_updates": country_rule_set_updates,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_rcs_agent(
        self,
        rcs_agent_id: "capo_pinpoint_sms_voice_v2.types.rcs_agent_id_or_arn.RcsAgentIdOrArn",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        deletion_protection_enabled: Optional[bool] = None,
        opt_out_list_name: Optional[
            "capo_pinpoint_sms_voice_v2.types.opt_out_list_name_or_arn.OptOutListNameOrArn"
        ] = None,
        self_managed_opt_outs_enabled: Optional[bool] = None,
        two_way_channel_arn: Optional[
            "capo_pinpoint_sms_voice_v2.types.two_way_channel_arn.TwoWayChannelArn"
        ] = None,
        two_way_channel_role: Optional[
            "capo_pinpoint_sms_voice_v2.types.iam_role_arn.IamRoleArn"
        ] = None,
        two_way_enabled: Optional[bool] = None,
        two_way_media_s3_bucket_name: Optional[
            "capo_pinpoint_sms_voice_v2.types.two_way_media_s3_bucket_name_or_unset.TwoWayMediaS3BucketNameOrUnset"
        ] = None,
        two_way_media_s3_key_prefix: Optional[
            "capo_pinpoint_sms_voice_v2.types.two_way_media_s3_key_prefix.TwoWayMediaS3KeyPrefix"
        ] = None,
        two_way_media_s3_role: Optional[
            "capo_pinpoint_sms_voice_v2.types.iam_role_arn_or_unset.IamRoleArnOrUnset"
        ] = None,
        two_way_rcs_events_enabled: Optional[
            "capo_pinpoint_sms_voice_v2.types.rcs_event_type_list.RcsEventTypeList"
        ] = None,
    ) -> (
        "capo_pinpoint_sms_voice_v2.types.update_rcs_agent_result.UpdateRcsAgentResult"
    ):
        """<p>Updates the configuration of an existing RCS agent. You can update the opt-out list, deletion protection, two-way messaging settings, and self-managed opt-outs configuration.</p>

        Args:
            rcs_agent_id: <p>The unique identifier of the RCS agent to update. You can use either the RcsAgentId or RcsAgentArn.</p>
            deletion_protection_enabled: <p>By default this is set to false. When set to true the RCS agent can't be deleted.</p>
            opt_out_list_name: <p>The OptOutList to associate with the RCS agent. Valid values are either OptOutListName or OptOutListArn.</p>
            self_managed_opt_outs_enabled: <p>By default this is set to false. When set to true you're responsible for responding to HELP and STOP requests. You're also responsible for tracking and honoring opt-out requests.</p>
            two_way_channel_arn: <p>The Amazon Resource Name (ARN) of the two way channel.</p>
            two_way_channel_role: <p>An optional IAM Role Arn for a service to assume, to be able to post inbound SMS messages.</p>
            two_way_enabled: <p>By default this is set to false. When set to true you can receive incoming text messages from your end recipients.</p>
            two_way_media_s3_bucket_name: <p>The name of the S3 bucket where inbound RCS media files are stored. Two-way messaging must be enabled on the agent. To remove the media configuration, pass the sentinel value <code>UNSET_RCS_MEDIA_CONFIGURATION</code> for both this field and TwoWayMediaS3Role.</p>
            two_way_media_s3_key_prefix: <p>The key prefix used for inbound RCS media objects in the S3 bucket.</p>
            two_way_media_s3_role: <p>The ARN of the IAM role used to write inbound RCS media files to the S3 bucket. The role must have <code>s3:PutObject</code> permission on the bucket and a trust policy allowing <code>sms-voice.amazonaws.com</code> to assume it. To remove the media configuration, pass the sentinel value <code>UNSET_RCS_MEDIA_CONFIGURATION</code> for both this field and TwoWayMediaS3BucketName.</p>
            two_way_rcs_events_enabled: <p>The list of RCS event types to enable for two-way messaging. Pass an empty list to disable all event types. The special value <code>ALL</code> enables all current and future event types and must be the sole element if used.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.update_rcs_agent_request.UpdateRcsAgentRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.update_rcs_agent_result.UpdateRcsAgentResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.update_rcs_agent

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.update_rcs_agent.async_update_rcs_agent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.update_rcs_agent_request.UpdateRcsAgentRequest = {
            "rcs_agent_id": rcs_agent_id
        }
        if deletion_protection_enabled is not None:
            input_["deletion_protection_enabled"] = deletion_protection_enabled
        if opt_out_list_name is not None:
            input_["opt_out_list_name"] = opt_out_list_name
        if self_managed_opt_outs_enabled is not None:
            input_["self_managed_opt_outs_enabled"] = self_managed_opt_outs_enabled
        if two_way_channel_arn is not None:
            input_["two_way_channel_arn"] = two_way_channel_arn
        if two_way_channel_role is not None:
            input_["two_way_channel_role"] = two_way_channel_role
        if two_way_enabled is not None:
            input_["two_way_enabled"] = two_way_enabled
        if two_way_media_s3_bucket_name is not None:
            input_["two_way_media_s3_bucket_name"] = two_way_media_s3_bucket_name
        if two_way_media_s3_key_prefix is not None:
            input_["two_way_media_s3_key_prefix"] = two_way_media_s3_key_prefix
        if two_way_media_s3_role is not None:
            input_["two_way_media_s3_role"] = two_way_media_s3_role
        if two_way_rcs_events_enabled is not None:
            input_["two_way_rcs_events_enabled"] = two_way_rcs_events_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_sender_id(
        self,
        sender_id: "capo_pinpoint_sms_voice_v2.types.sender_id_or_arn.SenderIdOrArn",
        iso_country_code: "capo_pinpoint_sms_voice_v2.types.iso_country_code.IsoCountryCode",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
        deletion_protection_enabled: Optional[bool] = None,
    ) -> (
        "capo_pinpoint_sms_voice_v2.types.update_sender_id_result.UpdateSenderIdResult"
    ):
        """<p>Updates the configuration of an existing sender ID.</p>

        Args:
            sender_id: <p>The sender ID to update.</p>
            iso_country_code: <p>The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.</p>
            deletion_protection_enabled: <p>By default this is set to false. When set to true the sender ID can't be deleted.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.update_sender_id_request.UpdateSenderIdRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.update_sender_id_result.UpdateSenderIdResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.update_sender_id

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.update_sender_id.async_update_sender_id(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.update_sender_id_request.UpdateSenderIdRequest = {
            "sender_id": sender_id,
            "iso_country_code": iso_country_code,
        }
        if deletion_protection_enabled is not None:
            input_["deletion_protection_enabled"] = deletion_protection_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def verify_destination_number(
        self,
        verified_destination_number_id: "capo_pinpoint_sms_voice_v2.types.verified_destination_number_id_or_arn.VerifiedDestinationNumberIdOrArn",
        verification_code: "capo_pinpoint_sms_voice_v2.types.verification_code.VerificationCode",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceV2ClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice_v2.types.verify_destination_number_result.VerifyDestinationNumberResult":
        """<p>Use the verification code that was received by the verified destination phone number to opt-in the verified destination phone number to receive more messages.</p>

        Args:
            verified_destination_number_id: <p>The unique identifier for the verififed destination phone number.</p>
            verification_code: <p>The verification code that was received by the verified destination phone number.</p>

        Raises:
            capo_pinpoint_sms_voice_v2.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient permissions to access the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.</p>
            capo_pinpoint_sms_voice_v2.errors.internal_server_exception.InternalServerException: <p>The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.</p>
            capo_pinpoint_sms_voice_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource couldn't be found.</p>
            capo_pinpoint_sms_voice_v2.errors.throttling_exception.ThrottlingException: <p>An error that occurred because too many requests were sent during a certain amount of time.</p>
            capo_pinpoint_sms_voice_v2.errors.validation_exception.ValidationException: <p>A validation exception for a field.</p>
            capo_pinpoint_sms_voice_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice_v2.types.verify_destination_number_request.VerifyDestinationNumberRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice_v2.types.verify_destination_number_result.VerifyDestinationNumberResult"
        ]:
            import capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.verify_destination_number

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice_v2._operations.pinpoint_sms_voice_v2.verify_destination_number.async_verify_destination_number(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice_v2.types.verify_destination_number_request.VerifyDestinationNumberRequest = {
            "verified_destination_number_id": verified_destination_number_id,
            "verification_code": verification_code,
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
